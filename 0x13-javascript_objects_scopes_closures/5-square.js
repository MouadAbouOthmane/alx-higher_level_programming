#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (s) {
    super(s, s);
    this.size = s;
  }
}

module.exports = Square;
