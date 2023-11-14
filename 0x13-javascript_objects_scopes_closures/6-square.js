#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    let l;
    if (c) {
      l = c;
    } else {
      l = 'X';
    }

    for (let i = 0, k = ''; i < this.width; k = '', i++) {
      for (let j = 0; j < this.height; k += l, j++);
      console.log(k);
    }
  }
}

module.exports = Square;
