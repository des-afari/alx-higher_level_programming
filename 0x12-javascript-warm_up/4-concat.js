#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const firstArg = argv[2] || 'undefined';
const secondArg = argv[3] || 'undefined';

console.log(firstArg + ' is ' + secondArg);
