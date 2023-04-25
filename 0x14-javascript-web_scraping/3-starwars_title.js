#!/usr/bin/node
/* prints the title of a Star Wars movie where episode number matches a given integer */
const request = require('request');

if (process.argv.length >= 3) {
  const _id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + _id;
  request(url, (err, response, body) => {
    if (err) throw err;
    const data = JSON.parse(body);
    console.log(data.title);
  });
}
