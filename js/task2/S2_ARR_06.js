// S2_ARR_06 — Transform records

function transformUsers(users) {
  return users
    .filter(user => user.active)
    .map(user => user.name.toUpperCase())
    .sort();
}

// Tests
const users = [
  { id: 1, name: "Alice", active: true },
  { id: 2, name: "bob", active: false },
  { id: 3, name: "charlie", active: true },
  { id: 4, name: "Dave", active: true },
];

console.log(transformUsers(users));
// ["ALICE", "CHARLIE", "DAVE"]
