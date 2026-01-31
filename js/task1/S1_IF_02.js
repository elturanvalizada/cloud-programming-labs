// S1_IF_02 — Score to grade

function grade(score) {
  if (score < 0 || score > 100) {
    return null;
  }

  if (score >= 90) {
    return "A";
  } else if (score >= 80) {
    return "B";
  } else if (score >= 70) {
    return "C";
  } else if (score >= 60) {
    return "D";
  } else {
    return "F";
  }
}

// Tests
console.log(grade(95));   // A
console.log(grade(85));   // B
console.log(grade(75));   // C
console.log(grade(65));   // D
console.log(grade(45));   // F
console.log(grade(-5));   // null
console.log(grade(120));  // null
