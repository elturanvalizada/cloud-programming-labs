// S1_VAR_10 — Mini debugger

function inspect(value) {
  return {
    type: value === null ? "null" : typeof value,
    isArray: Array.isArray(value),
    isNull: value === null,
    isNaN: typeof value === "number" && Number.isNaN(value),
  };
}

const tests = [
  null,
  undefined,
  0,
  NaN,
  "text",
  [],
  {},
  () => {},
];

for (const v of tests) {
  console.log(v, "=>", inspect(v));
}
