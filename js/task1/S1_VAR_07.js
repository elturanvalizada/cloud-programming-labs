// S1_VAR_07 — Coercion via unary plus

function toNumberOrNull(x) {
  if (typeof x !== "string") return null;

  const n = +x;
  if (Number.isNaN(n)) return null;

  return n;
}

const tests = [
  "12",
  "12.5",
  " 12 ",
  "12x",
  "",
  " ",
  null,
  undefined,
];

for (const v of tests) {
  console.log(JSON.stringify(v), "=>", toNumberOrNull(v));
}
