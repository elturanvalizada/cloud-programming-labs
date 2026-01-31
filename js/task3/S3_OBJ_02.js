// S3_OBJ_02 — Merge config (shallow)

function mergeDefaults(defaults, overrides) {
  return {
    ...defaults,
    ...overrides,
  };
}

// Tests
const defaults = {
  host: "localhost",
  port: 8080,
  debug: false,
};

const overrides = {
  port: 3000,
  debug: true,
};

const merged = mergeDefaults(defaults, overrides);

console.log(merged);
// { host: 'localhost', port: 3000, debug: true }

// Ensure inputs not mutated
console.log(defaults);  // unchanged
console.log(overrides); // unchanged
