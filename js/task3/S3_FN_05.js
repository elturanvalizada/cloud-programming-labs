// S3_FN_05 — Higher-order predicate

const atLeast = (min) => (value) => value >= min;

// Tests
const nums = [1, 3, 5, 7, 9];

console.log(nums.filter(atLeast(5)));   // [5, 7, 9]
console.log(nums.filter(atLeast(8)));   // [9]
console.log(nums.filter(atLeast(10)));  // []
