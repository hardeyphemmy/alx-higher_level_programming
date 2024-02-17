#!/usr/bin/node

exports.esrever = function (list) {
  // create an array to store reverse elemen
  const reversedList = [];
  // loop over original list
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
