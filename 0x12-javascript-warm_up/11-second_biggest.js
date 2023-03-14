#!/usr/bin/node
const size = process.argv.length;

if (size - 2 <= 1) {
  console.log('0');
} else {
  const numarr = process.argv.slice(2, size).sort((a, b) => b - a);
  const secmaxnum = numarr[1];
  console.log(secmaxnum);
}
