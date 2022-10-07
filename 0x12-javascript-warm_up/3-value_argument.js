#!/usr/bin/node
const arg = process.argv;
if (arg !== process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
