// S1_IF_03 — Truthy/falsy guard

function normalizeName(input) {
  if (!input) {
    return "Anonymous";
  }

  const trimmed = input.trim();
  return trimmed ? trimmed : "Anonymous";
}

// Tests
console.log(normalizeName(""));        // Anonymous
console.log(normalizeName(" "));       // Anonymous
console.log(normalizeName(null));      // Anonymous
console.log(normalizeName(" Ola "));   // Ola
