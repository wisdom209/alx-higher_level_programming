#!/usr/bin/node
if (process.argv[2]) {
  const toNum = Number(process.argv[2]);
  if (toNum) { console.log('My number:', toNum); } else { console.log('Not a number'); }
}
