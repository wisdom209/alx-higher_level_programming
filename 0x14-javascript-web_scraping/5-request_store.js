#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length >= 4) {
  const url = process.argv[2];
  const path = process.argv[3];

  request(url, (err, response, body) => {
    if (err == null) {
      fs.writeFile(path, body, err => {
        if (err) throw err;
      });
    }
  });
}
