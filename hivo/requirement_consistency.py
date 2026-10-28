"""Conservative source-bound incompatibility witnesses; no model or mutation.

Different properties are not alternatives. Unsupported semantics stay unknown;
only aligned target/property/condition constraints can prove a conflict here.
This is deliberately a bounded grammar, not a general natural-language solver.
"""
import json
import ast
import re

FILE = r'[\w./-]+\.[A-Za-z][A-Za-z0-9]*'
NUM = r'(?:one|two|three|four|five|six|seven|eight|nine|ten|\d+)'
NUMBERS = dict(zip('one two three four five six seven eight nine ten'.split(), range(1, 11)))


def _number(value):
    return NUMBERS[value.lower()] if value.lower() in NUMBERS else int(value)


def targets(text):
    return set(re.findall(FILE, text.lower()))


def condition(text):
    match = re.search(r'\b(?:if|when|unless|before|after|during)\b\s+(.+?)(?:[.;]|$)', text, re.I)
    return re.sub(r'\W+', ' ', match[0].lower()).strip() if match else 'unconditional'


def _literal_values(text):
    rows=[];ranges=[]
    for match in re.finditer(r'(?i)('+FILE+r')[\s\S]*?containing\s+exactly\s*:\s*("(?:[^"\\]|\\.)*")',text):
        try:rows.append((match[1].lower(),json.loads(match[2])));ranges.append(match.span(2))
        except ValueError:pass
    expanded=re.search(r'(?i)^The content of the file must be exactly\s+(.+?)\.?$',text)
    if expanded:
        try:rows.append((None,ast.literal_eval(expanded[1])));ranges.append(expanded.span(1))
        except (ValueError,SyntaxError):pass
    for start,end in sorted(ranges,reverse=True):text=text[:start]+' '*(end-start)+text[end:]
    return text,rows


def instruction_text(text):
    return _literal_values(text)[0]


def facts(text, default_target='artifact-set'):
    """Return explicit typed facts, preserving literal values without case folding."""
    text,literal_values=_literal_values(text)
    names = targets(text)
    scope = tuple(sorted(names)) if names else (default_target,)
    result = []
    def add(prop, value, target=scope):
        result.append({'target':target, 'property':prop, 'value':value, 'condition':condition(text)})
    for match in re.finditer(r'\bexactly\s+('+NUM+r')\s+(?:(?:UTF-?8|text|task|new)\s+)*(?:files?|artifacts?)\b', text, re.I):
        add('artifact_count', _number(match[1]), ('artifact-set',))
    for match in re.finditer(r'\b(LF|CRLF)(?:[- ]only)?\b', text, re.I):
        if re.search(r'(?i)\b(?:use|only|separator|ending)\b', text):add('line_endings', match[1].upper())
    if re.search(r'(?i)\b(?:no|without)\s+(?:a\s+)?(?:trailing|final)\s+newline', text):add('final_newline', False)
    elif re.search(r'(?i)\b(?:include|add|with|use)\s+(?:a\s+)?(?:trailing|final)\s+newline', text):add('final_newline', True)
    for name,value in literal_values:add('exact_content',value,(name,) if name else scope)
    # Prohibition/preservation and action are aligned by their full object,
    # not by a bag-of-words intersection ("additional files" != "a file").
    for clause in re.split(r'[;\n]|\.(?:\s|$)|\s+and\s+(?=(?:do not|must not|never)\b)', text, flags=re.I):
        match = re.search(r'(?i)\b(?P<negative>(?:(?:do|must|should|shall)\s+not|not|never)\s+)?(?P<verb>include|contain|exclude|prohibit|forbid|create|modify|change|update|delete|remove|preserve|keep)\s+(?P<object>.+)', clause)
        if not match:continue
        verb = match['verb'].lower();obj = match['object'].strip().rstrip('.')
        obj = re.sub(r'(?i)\b(?:must|should)\s+(?:remain|be)\s+unchanged\b', '', obj).strip()
        named = targets(obj)
        key = tuple(sorted(named)) if named else (re.sub(r'(?i)^(?:the|a|an)\s+', '', obj).lower(),)
        if verb in {'modify','change','update','preserve','keep','delete','remove'}:
            if named or verb in {'delete','remove','preserve','keep'}:
                add('mutation', not (verb in {'preserve','keep'} or bool(match['negative'])), key)
        if verb in {'include','contain','exclude','prohibit','forbid'}:
            add('includes:'+re.sub(r'(?i)^(?:the\s+)?(?:line\s+)?', '', obj).strip('"\'').lower(),
                (verb in {'include','contain'}) != bool(match['negative']))
        if verb == 'create':add('create', not bool(match['negative']), key)
    unchanged = re.search(r'(?i)(.+?)\s+(?:must\s+)?remain\s+unchanged', text)
    if unchanged:
        key = tuple(sorted(targets(unchanged[1]))) or (re.sub(r'(?i)^the\s+', '', unchanged[1]).strip().lower(),)
        add('mutation', False, key)
    return result


def contradiction(left, right, default_target='artifact-set'):
    for a in facts(left, default_target):
        for b in facts(right, default_target):
            if (a['target']==b['target'] and a['property']==b['property']
                    and a['condition']==b['condition'] and a['value']!=b['value']):
                return {'relationship':'CONFLICT', 'type':('opposite_polarity' if a['property'] in {'mutation','create'} or a['property'].startswith('includes:') else 'incompatible_'+a['property']),
                        'incompatibility':f"The same target {', '.join(a['target'])} has incompatible {a['property']} constraints under {a['condition']} conditions.",
                        'choice_a_effect':left, 'choice_b_effect':right, 'can_satisfy_both':False,
                        'constraint_witness':{'left':a,'right':b}}
    return None
