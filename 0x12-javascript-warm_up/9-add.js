#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (!arg1 || !arg2) {
  console.log('NaN');
} else {
  console.log(parseInt(arg1) + parseInt(arg2));
}
