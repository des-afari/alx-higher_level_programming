#!/usr/bin/node

const argv = process.argv[2];

if (Number.isInteger(Number(argv)) === true) {
  for (let i = 0; i < argv; i++) {
    let value = '';
    for (let j = 0; j < argv; j++) {
      value += 'X';
    }
    console.log(value);
  }
} else {
  console.log('Missing size');
}
