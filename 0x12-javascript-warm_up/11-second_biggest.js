#!/usr/bin/node

// Search the second biggest integer

// convert to integer and filter non integer
const nums = process.argv.slice(2).map(Number).filter(num => !isNaN(num));
// If no arg passed print 0
if (nums.length < 2) {
  console.log('0');
  process.exit(1);
}
// sort num in descending order
nums.sort((a, b) => b - a);
// print second largest
console.log('Second largest integer:', nums[1]);
