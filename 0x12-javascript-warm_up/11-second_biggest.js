#!/usr/bin/node

/* Convert command-line args to ints
 * slice used to create new array starting from 3rd element
 * applies number function into each element
 */
const numbers = process.argv.slice(2).map(Number);

if (numbers.length < 2) {
  console.log('0');
} else {
  /* Sorting the array in descending order */

  const sortedNumbers = numbers.sort((a, b) => b - a);

  console.log(sortedNumbers[1]);
}
