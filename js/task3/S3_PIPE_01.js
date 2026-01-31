// S3_PIPE_01 — pipe()

function pipe(...fns) {
  return (input) => {
    let value = input;
    for (const fn of fns) {
      value = fn(value);
    }
    return value;
  };
}

// Tests
const add1 = (n) => n + 1;
const double = (n) => n * 2;
const toStr = (n) => String(n);

const f = pipe(add1, double, toStr);

console.log(f(3)); // "8"  -> (3+1)=4, *2=8, to string
