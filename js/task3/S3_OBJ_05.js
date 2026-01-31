// S3_OBJ_05 — Invert

function invert(obj) {
  const result = {};

  for (const key in obj) {
    const value = obj[key];

    if (result[value] === undefined) {
      result[value] = key;
    } else if (Array.isArray(result[value])) {
      result[value].push(key);
    } else {
      result[value] = [result[value], key];
    }
  }

  return result;
}

// Tests
console.log(invert({ a: 1, b: 2, c: 1 }));
// { '1': ['a', 'c'], '2': 'b' }

console.log(invert({ x: "red", y: "blue", z: "red" }));
// { red: ['x','z'], blue: 'y' }

console.log(invert({}));
