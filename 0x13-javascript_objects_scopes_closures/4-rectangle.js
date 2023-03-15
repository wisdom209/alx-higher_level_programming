#!/usr/bin/node

const Rectangle = class {
  constructor (w, h) {
    w = Number(w);
    h = Number(h);
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const tempSize = this.width;
    this.width = this.height;
    this.height = tempSize;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};

module.exports = Rectangle;
