#!/usr/bin/node
const data = require('./101-data');
const dict = data.dict;
const invertedDict = {};
for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const occurence = dict[key];
    if (!invertedDict[occurence]) {
      invertedDict[occurence] = [];
    }
    invertedDict[occurence].push(key);
  }
}
console.log(invertedDict);
