// S3_PIPE_02 — compose()

function compose(...fns) {
  return (input) => {
    let value = input;
    for (let i = fns.length - 1; i >= 0; i--) {
      value = fns[i](value);
    }
    return value;
  };
}

// Tests
const add1 = (n) => n + 1;
const double = (n) => n * 2;

const f = compose(add1, double);

console.log(f(3)); // add1(double(3)) => 7
