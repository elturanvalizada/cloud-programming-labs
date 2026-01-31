// S1_VAR_06 — NaN pitfalls

function classifyNumberLike(x) {
  if (typeof x === "number" && Number.isNaN(x)) {
    return "nan";
  }
  if (typeof x === "number") {
    return "number";
  }
  return "not-a-number";
}

const tests = [
  NaN,
  0,
  3.14,
  "0",
  "abc",
  undefined,
  null,
];

for (const v of tests) {
  console.log(v, "=>", classifyNumberLike(v));
}
