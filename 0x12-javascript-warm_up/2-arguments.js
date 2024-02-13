#!/usr/bin/node

// print message depending on args passed

const myVar = process.argv.length - 2;
if (myVar === 0) {
  console.log('No argument');
} else if (myVar === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
