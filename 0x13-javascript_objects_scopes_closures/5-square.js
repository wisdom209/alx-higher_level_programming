#!/usr/bin/node

const Rectangle = require('./4-rectangle');

const Square = class extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
    this.size = this.size * 2;
  }

  print () {
    super.print();
  }

  rotate () {
    super.rotate();
  }
};

module.exports = Square;
