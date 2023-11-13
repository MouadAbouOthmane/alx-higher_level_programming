#!/usr/bin/node
const { argv } = require('process');

let num = parseInt(argv[2]);

console.log(Number.isInteger(num) ? 'My number: ' + num : 'Not a number');
