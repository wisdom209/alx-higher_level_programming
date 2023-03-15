#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  let i;
  for (i = 0; i < size / 2; i++) {
    const temp = list[i];
    list[i] = list[size - i - 1];
    list[size - i - 1] = temp;
  }
  return list;
};
