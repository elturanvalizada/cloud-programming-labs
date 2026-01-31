// S1_VAR_04 — Safe type label

function typeLabel(value) {
  if (value === null) return "null";
  return typeof value;
}

const tests = [
  null,
  undefined,
  42,
  "42",
  true,
  {},
  [],
  (() => {}),
];

for (const v of tests) {
  console.log(v, "=>", typeLabel(v));
}

