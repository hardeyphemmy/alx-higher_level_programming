#!/usr/bin/node

// print a square

const numSquare = parseInt(process.argv[2]);

if (!isNaN(numSquare)) {
  for (let i = 0; i**2; i++) {
    let line = 'x';
    for (let j = 0; j < numSquare; j++) {
      line += 'x';
    }
    console.log('x');
  }
} else {
  console.log('Missing size');
}
