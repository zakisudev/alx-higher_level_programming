#!/usr/bin/node
const args = process.argv.slice(2);
let n = 0;
if (args.length > 1) {
  const num = args.map(Number);
  num.sort((a, b) => b - a);
  n = num[1];
}
console.log(n);
