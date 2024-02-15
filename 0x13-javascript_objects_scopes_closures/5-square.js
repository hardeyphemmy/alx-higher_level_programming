#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
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

// class square extends Rectangle
class Square extends Rectangle {
  constructor (size) {
    // call constructor of the parent class with size
    super(size, size);
  }
}

module.extends = Square;
