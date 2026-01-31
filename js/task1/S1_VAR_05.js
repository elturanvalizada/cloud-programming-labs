// S1_VAR_05 — Array vs object

function isArray(value) {
  return Array.isArray(value);
}

const tests = [
  [],
  [1, 2, 3],
  {},
  { a: 1 },
  "text",
  42,
  null,
  undefined,
];

for (const v of tests) {
  console.log(v, "=> isArray:", isArray(v));
}
