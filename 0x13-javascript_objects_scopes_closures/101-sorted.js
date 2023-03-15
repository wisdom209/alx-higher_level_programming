#!/usr/bin/node
const oldDict = require('./101-data.js').dict;
const newDict = {};

let i = 0;
for (i in oldDict) {
  const value = oldDict[i];
  const key = i;
  if (newDict[value]) {
    newDict[value] = [...newDict[value], key].sort((a, b) => a > b);
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
