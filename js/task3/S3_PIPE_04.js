// S3_PIPE_04 — Array processing pipeline

function pipe(...fns) {
  return (input) => fns.reduce((v, fn) => fn(v), input);
}

const filterValidNumbers = (arr) =>
  arr.filter(x => !Number.isNaN(Number(x)));

const toNumbers = (arr) =>
  arr.map(x => Number(x));

const doubleAll = (arr) =>
  arr.map(n => n * 2);

const sumAll = (arr) =>
  arr.reduce((sum, n) => sum + n, 0);

const processNumbers = pipe(
  filterValidNumbers,
  toNumbers,
  doubleAll,
  sumAll
);

// Tests
console.log(processNumbers(["1", "x", "2"]));        // 6  -> (1*2 + 2*2)
console.log(processNumbers(["3", "4.5", "bad"]));   // 15
console.log(processNumbers([]));                    // 0
