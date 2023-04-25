#!/usr/bin/node
/* display the status code of a GET request */
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  request(url, (err, response, body) => {
    if (err) throw err;
    console.log('code:', response.statusCode);
  });
}
