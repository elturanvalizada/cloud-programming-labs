// S2_FOR_03 — Sum until threshold

function sumUntil(nums, threshold) {
  let sum = 0;

  for (const n of nums) {
    if (sum + n > threshold) {
      break;
    }
    sum += n;
  }

  return sum;
}

// Tests
console.log(sumUntil([1, 2, 3, 4], 5));   // 3 (1+2, stop before 6)
console.log(sumUntil([2, 2, 2], 10));     // 6
console.log(sumUntil([5, 5, 5], 7));      // 5
console.log(sumUntil([], 10));            // 0
