// S3_PIPE_03 — String normalization pipeline

function pipe(...fns) {
  return (input) => fns.reduce((v, fn) => fn(v), input);
}

const trim = (s) => s.trim();
const lower = (s) => s.toLowerCase();
const collapseSpaces = (s) => s.replace(/\s+/g, " ");

const normalize = pipe(trim, lower, collapseSpaces);

// Tests
console.log(normalize("   HeLLo   WoRLD   ")); // "hello world"
console.log(normalize("A   B    C"));          // "a b c"
console.log(normalize("   ONE\tTWO  THREE ")); // "one two three"

