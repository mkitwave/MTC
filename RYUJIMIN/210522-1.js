//런타임에러
//const fs = require('fs');
//const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

function answer(input){
const input = ['5','55 185','58 183','88 186','60 175','60 175','46 155'];
const num = input.shift(); //인원수
const wh = input.map((wh1) => input.split(' ') //공백 단위로 잘라서 2차원 배열 만들기
                .map((num) => parseInt(num))); //정수형으로 변환하기
const answer = [];

for (var i = 0; i < num; i++){  //1명잡고
  const count = 0;  //순위카운트
  for (var j = 0; j < num; j++){  //나머지애들과 비교
    if(!i==j){  //동일인이 아닐때
      if(wh[i][0] < wh[j][0] && wh[i][1] < wh[j][1]){ //덩치가 작으면 카운트++
        count++;
      }
    }
  }
  answer.push(count+1); //카운트+1 : 순위
}

console.log(answer.join(' ')); //배열 공백구분으로 문자열 변환
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
  answer(list); 
  process.exit(); 
});