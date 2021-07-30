// https://programmers.co.kr/learn/courses/30/lessons/12931
function solution(n){
  var answer = 0;
  var num = n.toString().split('');
  for(var i=0; i<num.length; i++){
      answer += parseInt(num[i]);
  }

  return answer;
}