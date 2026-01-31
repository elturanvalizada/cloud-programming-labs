// S3_FN_06 — Map values

function mapValues(obj, fn) {
  const result = {};

  for (const key in obj) {
    result[key] = fn(obj[key]);
  }

  return result;
}

// Tests
const numbers = { a: 1, b: 2, c: 3 };
const doubled = mapValues(numbers, x => x * 2);

console.log(doubled);   // { a: 2, b: 4, c: 6 }
console.log(numbers);  // unchanged

const words = { x: "hi", y: "hello" };
console.log(mapValues(words, s => s.toUpperCase()));
// { x: 'HI', y: 'HELLO' }
