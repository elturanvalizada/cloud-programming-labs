// S3_FN_02 — Sort by property

const people = [
  { name: "Alice", age: 30 },
  { name: "Bob", age: 22 },
  { name: "Charlie", age: 25 },
];

// Use arrow function comparator
const sortedByAge = [...people].sort((a, b) => a.age - b.age);

// Tests
console.log(sortedByAge);
// [
//   { name: 'Bob', age: 22 },
//   { name: 'Charlie', age: 25 },
//   { name: 'Alice', age: 30 }
// ]

// Ensure original array not mutated
console.log(people);
