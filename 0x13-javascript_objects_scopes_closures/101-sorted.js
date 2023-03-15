#!/usr/bin/node
const oldDict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
const newDict = {};

let i = 0;
for (i in oldDict) {
  const value = oldDict[i];
  const key = i;
  if (newDict[value]) {
    newDict[value] = [...newDict[value], key];
  } else {
    newDict[value] = [key];
  }
}

console.log(newDict);
