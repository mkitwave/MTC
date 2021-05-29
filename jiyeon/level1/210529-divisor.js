// https://programmers.co.kr/learn/courses/30/lessons/12928

function solution(n) {
  var answer = 0;
  for(var i = 0; i <= n; i++){
      if(n % i == 0){
          answer += i;
      }
  }
  return answer;
}