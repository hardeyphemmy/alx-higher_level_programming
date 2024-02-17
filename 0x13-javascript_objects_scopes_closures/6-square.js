#!/usr/bin/node

// Import Square from 5-square
const ParentSquare = require('./5-square');

// Define class square extends parentsquare
class Square extends ParentSquare {
  constructor (size) {
    // call constructor of the parent class with size
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
