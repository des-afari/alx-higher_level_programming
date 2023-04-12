#!/usr/bin/node

const process = require('process');
const argv = process.argv[2];

if (Number.isInteger(Number(argv)) === true) {
  console.log('My number:', argv);
} else {
  console.log('Not a number');
}
