#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const filename = process.argv[2];
const buffer = process.argv[3];

fs.writeFile(filename, buffer, (err) => {
  if (err) console.log(err);
});
