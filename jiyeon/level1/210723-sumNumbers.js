// https://programmers.co.kr/learn/courses/30/lessons/12912
function solution(a, b) {
  var answer = 0;
  var temp = 0;
  
  if(a > b){
      temp = a;
      a = b;
      b = temp;
  }        
  
  for (var i=a; i<=b; i++) answer += i;
  
  return answer;
}