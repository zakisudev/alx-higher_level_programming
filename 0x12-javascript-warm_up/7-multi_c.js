#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < x; y++) {
    console.log('C is fun');
  }
}
