#!/usr/bin/node
const ParentSquare = require('./5-square');

const Square = class extends ParentSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let i;
    let j;
    for (i = 0; i < this.size; i++) {
      for (j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
};

module.exports = Square;
