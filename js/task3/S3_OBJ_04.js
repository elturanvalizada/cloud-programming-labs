// S3_OBJ_04 — Omit

function omit(obj, keys) {
  const result = {};

  for (const key in obj) {
    if (!keys.includes(key)) {
      result[key] = obj[key];
    }
  }

  return result;
}

// Tests
const user = {
  id: 1,
  name: "Alice",
  role: "admin",
  active: true,
};

console.log(omit(user, ["role"]));
// { id: 1, name: 'Alice', active: true }

console.log(omit(user, ["id", "active"]));
// { name: 'Alice', role: 'admin' }

console.log(omit(user, []));
// { id: 1, name: 'Alice', role: 'admin', active: true }
