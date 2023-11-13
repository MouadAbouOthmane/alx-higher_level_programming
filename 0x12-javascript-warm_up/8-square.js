#!/usr/bin/node
const { argv } = require('process');

const num = parseInt(argv[2]);

if (num) {
  for (let i = 0; i < num; i++) {
    let x = '';
    for (let j = 0; j < num; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
