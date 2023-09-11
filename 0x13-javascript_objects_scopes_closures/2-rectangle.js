#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      // If w or h is not a positive integer, create an empty object
      return this;
    }
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
