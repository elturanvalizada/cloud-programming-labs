// S3_FN_04 — Map / filter / reduce with arrows

const sumOfSquaresOfEvens = (nums) =>
  nums
    .filter(n => n % 2 === 0)
    .map(n => n * n)
    .reduce((sum, n) => sum + n, 0);

// Tests
console.log(sumOfSquaresOfEvens([1, 2, 3, 4]));     // 20 (2^2 + 4^2)
console.log(sumOfSquaresOfEvens([2, 4, 6]));        // 56
console.log(sumOfSquaresOfEvens([1, 3, 5]));        // 0
console.log(sumOfSquaresOfEvens([]));               // 0
