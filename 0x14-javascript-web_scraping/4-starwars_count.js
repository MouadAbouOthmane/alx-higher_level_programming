#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];
const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let numMovie = 0;

    data.forEach(el => {
      if (el.characters.indexOf(charUrl) !== -1) numMovie++;
    });
    console.log(numMovie);
  }
});
