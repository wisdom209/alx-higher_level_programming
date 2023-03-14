#!/usr/bin/node
// Executes theFunction 'x' times
exports.callMeMoby = function (x, func) {
  let i = x - 1;
  while (i >= 0) {
    func();
    i--;
  }
};
