#!/usr/bin/node

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);

if (!isNaN(num) && Number.isInteger(num) && num >= 0) {
  console.log(factorial(num));
} else {
  console.log('1');
}
