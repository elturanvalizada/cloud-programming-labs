// S3_PIPE_06 — Safe pipeline

function pipeSafe(...fns) {
  return (input) => {
    let value = input;

    try {
      for (const fn of fns) {
        value = fn(value);
      }
      return { ok: true, value };
    } catch (error) {
      return { ok: false, error: error instanceof Error ? error.message : String(error) };
    }
  };
}

// Tests
const parseNumber = (x) => {
  const n = Number(x);
  if (Number.isNaN(n)) throw new Error("Not a number");
  return n;
};

const inverse = (n) => {
  if (n === 0) throw new Error("Division by zero");
  return 1 / n;
};

const safeProcess = pipeSafe(parseNumber, inverse);

console.log(safeProcess("4"));   // { ok: true, value: 0.25 }
console.log(safeProcess("0"));   // { ok: false, error: 'Division by zero' }
console.log(safeProcess("x"));   // { ok: false, error: 'Not a number' }
