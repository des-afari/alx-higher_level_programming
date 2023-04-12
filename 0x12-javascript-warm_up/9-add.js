#!/usr/bin/node

function add (a, b) {
  const argv = process.argv;

  try {
    a = argv[2];
    b = argv[3];

    console.log(Number(a) + Number(b));
  } catch (err) {
    console.log(NaN);
  }
}

add();
