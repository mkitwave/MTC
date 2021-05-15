const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').split('\n');

let N = Number(input[0]);
const data = input[1].split(' ').map(n => Number(n));
data.sort((a, b) => a - b);

let result = 0;
let count = 0;

for (let i = 0; i < data.length; i++) {
  count += 1;
  if (count >= data[i]) {
    result += 1;
    count = 0;
  }
}

console.log(result);
