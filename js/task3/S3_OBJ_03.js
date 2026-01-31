// S3_OBJ_03 — Pick

function pick(obj, keys) {
  const result = {};

  for (const key of keys) {
    if (key in obj) {
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

console.log(pick(user, ["id", "name"]));
// { id: 1, name: 'Alice' }

console.log(pick(user, ["name", "email"]));
// { name: 'Alice' }

console.log(pick(user, []));
// {}
