#!/usr/bin/node

// print the first arg passed

if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
