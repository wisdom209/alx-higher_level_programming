#!/usr/bin/node
exports.converter = function (base) {
  const convertNum = function (num) {
    return num.toString(base);
  };
  return convertNum;
};
