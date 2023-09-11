#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  add: function () {
    this.value += 1;
  }
};
console.log(myObject);
myObject.add();
console.log(myObject);
myObject.add();
console.log(myObject);
myObject.add();
console.log(myObject);
