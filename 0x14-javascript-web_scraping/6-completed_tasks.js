#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    const ob = {};

    data.forEach(el => {
      if (el.completed) {
        if (el.userId in ob) ob[el.userId] += 1;
        else ob[el.userId] = 1;
      }
    });

    console.log(ob);
  }
});
