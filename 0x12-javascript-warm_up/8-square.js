#!/usr/bin/node
const size = Number(process.argv[2]);
let i = 0;
let j = 0;
if (size) {
  while (i < size) {
    j = 0;
    while (j < size) {
      process.stdout.write('X');
      j++;
    }
    console.log();
    i++;
  }
} else {
  console.log('Missing size');
}
