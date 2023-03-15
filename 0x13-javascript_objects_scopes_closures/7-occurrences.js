#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let counter = 0;
  const listLen = list.length;

  for (x = 0; x < listLen; x++) {
    if (list[x] === searchElement) {
      counter++;
    }
  }
  return (counter);
};
