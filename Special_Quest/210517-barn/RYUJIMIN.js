//백준손절

function solution(list) {
  let x = parseInt(list[1]/list[3]) * parseInt(list[2]/list[3]);
  console.log(Math.min(list[0], x));
} 

const readline = require("readline"); 
const rl = readline.createInterface({
  input: process.stdin, 
  output: process.stdout, 
}); 

let input; 
let list = []; 
rl.on("line", function (line) {
  input = line; 
  rl.close(); 
}).on("close", function () {
  list.push(input.split(' ').map((el) => el)); 
  list.push(input.split(' ').map((el) => parseInt(el))); 
  solution(list); 
  process.exit(); 
});
