// S1_VAR_08 — Big integers

function safeAdd(a, b) {
  const bothIntegers = Number.isInteger(a) && Number.isInteger(b);

  if (
    bothIntegers &&
    (Math.abs(a) > Number.MAX_SAFE_INTEGER ||
      Math.abs(b) > Number.MAX_SAFE_INTEGER)
  ) {
    const result = BigInt(a) + BigInt(b);
    console.log("Returned type: BigInt");
    return result;
  }

  const result = a + b;
  console.log("Returned type: Number");
  return result;
}

const tests = [
  [1, 2],
  [Number.MAX_SAFE_INTEGER, 1],
  [9007199254740993, 1],
  [10.5, 2],
];

for (const [a, b] of tests) {
  console.log(`${a} + ${b} =`, safeAdd(a, b));
}
