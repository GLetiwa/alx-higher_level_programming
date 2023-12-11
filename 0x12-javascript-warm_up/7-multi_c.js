#!/usr/bin/node

const number = parseInt(process.argv[2]);

if (!isNaN(number)) {
  for (let x = 0; x < number; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
