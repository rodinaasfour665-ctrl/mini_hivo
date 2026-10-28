"""Workspace-bound, auditable continuation for explicit requirement decisions.

Original text/ledger are retained. Only an explicitly confirmed losing statement
is superseded in the execution input; unrelated statements remain byte-for-byte.
"""
import hashlib
import json
from pathlib import Path
import re


class RequirementDecisions:
    def __init__(self, workspace):
        self.identity=hashlib.sha256(str(Path(workspace).resolve()).casefold().encode()).hexdigest()
        self.path=Path(workspace)/'.hivo/requirement-decisions.json'

    def load(self):
        try:
            state=json.loads(self.path.read_text(encoding='utf-8'))
            if state.get('workspace_id')==self.identity and state.get('status')=='pending':return state
        except (OSError,ValueError,AttributeError):pass

    def save(self,state):
        state['workspace_id']=self.identity
        self.path.parent.mkdir(parents=True,exist_ok=True)
        payload=json.dumps(state,ensure_ascii=False)
        with self.path.with_suffix('.history.jsonl').open('a',encoding='utf-8',newline='\n') as f:f.write(payload+'\n')
        temp=self.path.with_suffix('.tmp');temp.write_text(payload,encoding='utf-8');temp.replace(self.path)

    def is_new_task(self,text,state):
        if re.match(r'(?i)^\s*new\s+task\s*:',text):return True
        if text.strip()==state['original_request'].strip():return False
        choices=[x for q in state['questions'] for x in q.get('options',[])]
        return text.strip() not in choices and bool(re.match(r'(?i)^\s*(?:create|build|implement|make)\b',text))

    def accept(self,state,answers):
        from .requirement_consistency import contradiction
        for record in answers:
            question=next((q for q in state['questions'] if q['question_id']==record.get('question_id')),None)
            if not question:continue
            text=str(record.get('answer','')).strip();options=question.get('options',[])
            choice=next((i for i,x in enumerate(options) if text==x),None)
            if choice is None and len(options)==2:
                rejected=[i for i,x in enumerate(options) if contradiction(text,x)]
                if len(rejected)==1:choice=1-rejected[0]
            if choice is not None:
                state['answers'][question['question_id']]=dict(record, selected_index=choice)

    def parse_answer(self,text,state):
        unresolved=[q for q in state['questions'] if q['question_id'] not in state['answers']]
        try:values=json.loads(text)
        except ValueError:values=None
        if not isinstance(values,dict):
            match=re.match(r'(?is)^\s*(Q-\d+)\s*:\s*(.+)',text)
            values={match[1]:match[2]} if match else ({unresolved[0]['question_id']:text} if len(unresolved)==1 else {})
        result=[]
        for q in unresolved:
            value=values.get(q['question_id'])
            if value is None:continue
            value=str(value).strip()
            if value.lower() in {'1','first','option 1'}:value=q['options'][0]
            elif value.lower() in {'2','second','option 2'}:value=q['options'][1]
            result.append({'question_id':q['question_id'],'answer':value,'selected_option':value,
                           'affected_requirement_ids':q['affected_requirement_ids'],'provenance':'USER_CONFIRMED','phase':'REQUEST_CLARIFICATION'})
        return result

    def effective_input(self,state):
        if any(q['question_id'] not in state['answers'] for q in state['questions']):return None
        retired=set();chosen=set()
        for q in state['questions']:
            ids=q['affected_requirement_ids'];index=state['answers'][q['question_id']]['selected_index']
            chosen.add(ids[index]);retired.add(ids[1-index])
        if chosen & retired:return None
        raw=state['original_request']
        for row in state['ledger']['requirements']:
            if row['requirement_id'] not in retired:continue
            pattern=r'\s+'.join(re.escape(x) for x in row.get('source_clause',row['text']).split())
            raw,count=re.subn(pattern,'',raw,count=1)
            if not count:return None  # Cannot map a decision back to its source safely.
        state['superseded_requirement_ids']=sorted(retired)
        state['status']='resolved'
        return raw
