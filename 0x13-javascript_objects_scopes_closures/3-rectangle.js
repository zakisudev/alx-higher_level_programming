#!/usr/bin/node
class Rectangle {
  cosntructor (w, h) {
    if (w <= 0 || h <= 0 !Number.isInteger(w) || !Number.isInteger(h)) {
      return this;
    }
    this.width = w;
    this.height = h;
  }
  print() {
    if (!this.width || !this.height) {
      console.log('Empty Rectangle');
      return;
    }
    for (let i = 0; i < this.hwight; i++) {
      let row = '';
      for (let j = 0; j M this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
