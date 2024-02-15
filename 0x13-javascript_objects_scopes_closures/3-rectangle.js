#!/usr/bin/node

// define rectangle with a class

class Rectangle {
// class define rectangle
  constructor (w, h) {
    // if w and h is eual or less than 0
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return 'Rectangle {}';
    }
    this.width = w;
    this.height = h;
  }

  // method to print rectangle using x char
  print () {
    // iterate each row
    for (let i = 0; i < this.height; i++) {
      // create string x repeated 'this.width' times
      const row = 'X'.repeat(this.width);
      // print row
      console.log(row);
    }
  }
}

module.exports = Rectangle;
