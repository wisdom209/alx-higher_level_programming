#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
if (fileC) {
  fs.readFile(fileA, 'utf-8', (err, data) => {
    if (!err) {
      fs.writeFile(fileC, data, { flag: 'a+' }, (err) => {
        if (err) { console.log(err); }
      });
    }
  });
  fs.readFile(fileB, 'utf-8', (err, data) => {
    if (!err) {
      fs.writeFile(fileC, data, { flag: 'a+' }, (err) => {
        if (err) { console.log(err); }
      });
    }
  });
}
