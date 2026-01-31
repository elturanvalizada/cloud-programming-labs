// S3_OBJ_06 — Group by

function groupBy(items, key) {
  const result = {};

  for (const item of items) {
    const value = item[key];

    if (result[value] === undefined) {
      result[value] = [];
    }

    result[value].push(item);
  }

  return result;
}

// Tests
const users = [
  { id: 1, name: "Alice", role: "admin" },
  { id: 2, name: "Bob", role: "user" },
  { id: 3, name: "Charlie", role: "admin" },
];

console.log(groupBy(users, "role"));
/*
{
  admin: [
    { id: 1, name: 'Alice', role: 'admin' },
    { id: 3, name: 'Charlie', role: 'admin' }
  ],
  user: [
    { id: 2, name: 'Bob', role: 'user' }
  ]
}
*/
