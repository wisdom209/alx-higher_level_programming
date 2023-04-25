#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');

if (process.argv.length >= 3) {
  const path = process.argv[2];

  fs.readFile(path, 'utf-8', function (err, data) {
    if (err) throw err;
    process.stdout.write(data);
  });
}
