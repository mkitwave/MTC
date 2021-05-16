// https://programmers.co.kr/learn/courses/30/lessons/42748

function solution(array, commands) {
  var answer = [];
  var result = [];
  for (var a = 0; a < commands.length; a++){
      var k = commands[a][2];
      answer = array.slice(commands[a][0] - 1, commands[a][1]);
      //핵심 코드...
      answer = answer.sort((a,b)=> a - b);
      answer.push(answer[k-1]);
  }
  
  return answer;
}