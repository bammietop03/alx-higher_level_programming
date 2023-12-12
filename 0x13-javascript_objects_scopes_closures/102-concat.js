#!/usr/bin/node

const fs = require('fs');

const [, , file1, file2, destination] = process.argv;

fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;

    const concatenatedData = `${data1}${data2}`;

    fs.writeFile(destination, concatenatedData, 'utf8', (err) => {
      if (err) throw err;
    });
  });
});
