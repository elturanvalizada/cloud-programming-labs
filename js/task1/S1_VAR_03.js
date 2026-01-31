// S1_VAR_03 — “const is not immutable”

const user = { name: "Ala", tags: [] };

// Mutating the object is allowed
user.tags.push("student");
user.tags.push("js");
console.log("After pushing tags:", user);

try {
  // Reassigning the const variable is NOT allowed
  user = {};
} catch (err) {
  console.log("Error on reassignment:", err.message);
}
