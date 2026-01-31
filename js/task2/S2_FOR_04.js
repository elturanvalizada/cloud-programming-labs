// S2_FOR_04 — Count occurrences

function countOccurrences(values) {
  const counts = {};

  for (const v of values) {
    if (counts[v] === undefined) {
      counts[v] = 1;
    } else {
      counts[v]++;
    }
  }

  return counts;
}

// Tests
console.log(countOccurrences([1, 2, 1, 3, 2, 1]));
// { '1': 3, '2': 2, '3': 1 }

console.log(countOccurrences(["a", "b", "a", "c", "b"]));
// { a: 2, b: 2, c: 1 }

console.log(countOccurrences([]));
// {}
