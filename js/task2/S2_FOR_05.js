// S2_FOR_05 — Multiplication table

for (let i = 1; i <= 10; i++) {
  let row = "";

  for (let j = 1; j <= 10; j++) {
    row += String(i * j).padStart(4, " ");
  }

  console.log(row);
}
