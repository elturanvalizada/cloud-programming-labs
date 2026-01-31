// S1_IF_01 — Shipping cost

function shippingCost(weightKg, isMember) {
  let cost;

  if (weightKg < 1) {
    cost = 10;
  } else if (weightKg <= 5) {
    cost = 20;
  } else {
    cost = 30;
  }

  if (isMember) {
    cost = cost * 0.8; // 20% discount
  }

  return cost;
}

// Tests
console.log(shippingCost(0.5, false)); // 10
console.log(shippingCost(3, false));   // 20
console.log(shippingCost(7, false));   // 30
console.log(shippingCost(3, true));    // 16
console.log(shippingCost(7, true));    // 24
