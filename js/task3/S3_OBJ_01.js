// S3_OBJ_01 — Safe read

function get(obj, path, fallback) {
  if (obj == null) return fallback;

  const parts = String(path).split(".");
  let current = obj;

  for (const key of parts) {
    if (current == null || !(key in Object(current))) {
      return fallback;
    }
    current = current[key];
  }

  return current;
}

// Tests
const data = { a: { b: { c: 42 }, d: null } };

console.log(get(data, "a.b.c", "X"));    // 42
console.log(get(data, "a.b.x", "X"));    // X
console.log(get(data, "a.d.c", "X"));    // X (because a.d is null)
console.log(get(null, "a.b.c", "X"));    // X
console.log(get(data, "a.b", "X"));      // { c: 42 }
