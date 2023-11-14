#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (s) {
    super(s, s);
  }
}

module.exports = Square;
