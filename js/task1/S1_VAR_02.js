// S1_VAR_02 — Block scope check

console.log("=== let example ===");

try {
  {
    let x = 10;
    console.log("Inside block (let):", x);
  }
  console.log("Outside block (let):", x);
} catch (err) {
  console.log("Error accessing let outside block:", err.message);
}

console.log("\n=== var example ===");

try {
  {
    var y = 20;
    console.log("Inside block (var):", y);
  }
  console.log("Outside block (var):", y);
} catch (err) {
  console.log("Error accessing var:", err.message);
}

/*
Explanation:
- let is block-scoped, so it is not accessible outside the block.
- var is function-scoped, so it remains accessible after the block.
*/
