#!/usr/bin/node

// Print a factorial

function factorial (n) {
  // if n is NaN or 0 fact is 1
  if (isNaN(n) || n === 0) {
    return 1;
  }
  // Recursive case: n(n-1)!
  return n * factorial(n - 1);
}
const num = parseInt(process.argv[2]);
// print the pactorial
console.log(factorial(num));
