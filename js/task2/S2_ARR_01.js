// S2_ARR_01 — Clean numbers
// Given an array of strings, return an array of numbers;
// drop any item that becomes NaN.

function cleanNumbers(arr) {
  const out = [];

  for (const s of arr) {
    const n = Number(s);
    if (!Number.isNaN(n)) out.push(n);
  }

  return out;
}

// Tests
console.log(cleanNumbers([" 1 ", "x", "2"]));     // [1, 2]
console.log(cleanNumbers(["3", "4.5", "abc"]));  // [3, 4.5]
console.log(cleanNumbers([" ", "", "7"]));       // [0, 0, 7]
