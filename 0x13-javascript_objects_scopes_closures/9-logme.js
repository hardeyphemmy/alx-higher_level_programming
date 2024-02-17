#!/usr/bin/node
// initialize num of argument
let count = 0;
// print argument already printed with current argument
exports.logMe = function (item) {
  // print current count and argument
  console.log(count + ': ' + item);
  // increment for next call
  count++;
};
