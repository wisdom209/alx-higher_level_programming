#!/usr/bin/node
const cmdLen = process.argv.length - 2;

if (cmdLen === 0) { console.log('No argument'); }
if (cmdLen === 1) { console.log('Argument found'); }
if (cmdLen > 1) { console.log('Arguments found'); }
