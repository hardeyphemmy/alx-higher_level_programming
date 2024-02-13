#!/usr/bin/node

// print a square

const numSquare = parseInt(process.argv[2]);

if (!isNaN(numSquare)) {
  for (let i = 0; i < numSquare; i++) {
    let row = '';
    for (let j = 0; j < numSquare; j++) {
      row += 'x';
    }
    console.log('row');
  }
} else {
  console.log('Missing size');
}
