#!/usr/bin/node
const num = Number(process.argv[2]);
let i = 0;
if (num) {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
