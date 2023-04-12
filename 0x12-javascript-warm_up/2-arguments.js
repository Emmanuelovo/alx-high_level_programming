#!/usr/bin/node

const tag = process.argv.slice(2);

if (tag.length === 0) {
  console.log('No argument');
} else if ( tag.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

