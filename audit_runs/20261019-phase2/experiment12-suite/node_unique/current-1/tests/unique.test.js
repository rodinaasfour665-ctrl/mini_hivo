const assert=require('node:assert/strict');
const {uniqueValues}=require('../values.js');
assert.deepEqual(uniqueValues([3,1,3,2,1]), [3,1,2]);
assert.deepEqual(uniqueValues(['b','a','b']), ['b','a']);
assert.deepEqual(uniqueValues([]), []);
const original=[2,1,2]; uniqueValues(original); assert.deepEqual(original,[2,1,2]);
console.log('unique behavior tests: 4 passed');
