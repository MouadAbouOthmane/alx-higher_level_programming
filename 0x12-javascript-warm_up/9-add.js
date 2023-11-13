#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  if (a && b) {
    console.log(a + b);
  } else {
    console.log('NaN');
  }
}

add(argv[2], argv[3]);
