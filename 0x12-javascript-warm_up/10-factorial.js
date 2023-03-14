#!/usr/bin/node
const num = Number(process.argv[2]);
function fact (n) {
  if (!n || n === 0) { return (1); }
  return n * fact(n - 1);
}
console.log(fact(num));
