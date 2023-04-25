#!/usr/bin/node
/* Script writes a string to a file */

const fs = require('fs');

if (process.argv.length >= 4) {
  const path = process.argv[2];
  const string = process.argv[3];

  fs.writeFile(path, string, err => {
    if (err) { console.log(err); }
  });
}
