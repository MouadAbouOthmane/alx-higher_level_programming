#!/usr/bin/node
const { argv } = require('process');

if (argv.length < 3) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < argv[2]; i++) {
  console.log('C is fun');
}
