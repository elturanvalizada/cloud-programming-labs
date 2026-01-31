// S1_VAR_01 — Declare & observe

var a = "hello";     // string
let b = 42;          // number
const c = true;      // boolean

const table = [
  { name: "a", value: a, type: typeof a },
  { name: "b", value: b, type: typeof b },
  { name: "c", value: c, type: typeof c },
];

console.table(table);
