#!/usr/bin/node
function addMaybe (num, theFunction) {
  num += 1;
  theFunction(num);
}
module.exports = {
	addMaybe;
}
