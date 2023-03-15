#!/usr/bin/node

exports.logMe = function loggerFunction (item) {
  if (typeof loggerFunction.counter === 'undefined') {
    loggerFunction.counter = 0;
  }
  console.log(`${loggerFunction.counter}: ${item}`);
  loggerFunction.counter++;
};
