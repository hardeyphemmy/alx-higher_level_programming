#!/usr/bin/node

// print two arguments in a is format

if (process.argv.length > 4) {
  console.log('usage: node script.js <argument1> <argument2>');
} else {
  console.log(`${process.argv[2]} is ${process.argv[3]}`);
}
