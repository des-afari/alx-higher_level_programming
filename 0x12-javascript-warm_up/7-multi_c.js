#!/usr/bin/node

const process = require('process');
const argv = process.argv[2];

if (Number.isInteger(Number(argv)) === true) {
  for (let i = 0; i < argv; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
