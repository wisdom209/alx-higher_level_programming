#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const newDict = {};

let i = 0;
for (i in oldDict) {
  const value = oldDict[i];
  const key = i;
  if (newDict[value]) {
    newDict[value] = [key, ...newDict[value]];
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
