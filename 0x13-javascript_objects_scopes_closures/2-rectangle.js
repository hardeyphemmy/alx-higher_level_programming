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
}

module.exports = Rectangle;
