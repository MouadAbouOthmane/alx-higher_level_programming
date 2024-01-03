#!/usr/bin/node

const process = require('process');
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, (err) => {
      if (err) console.log(err);
    });
  }
});
