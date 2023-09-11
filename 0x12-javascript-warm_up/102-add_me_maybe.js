#!/usr/bin/node
function addMaybe (number, theFunction) {
  number += 1;
  theFunction(number);
}
module.exports = {
	addMaybe;
}
