// https://programmers.co.kr/learn/courses/30/lessons/77884

function solution(left, right) {
  var answer = 0;
  
  for(var i = left; i <= right; i++){
      var count = 0;
      for (var j = 1; j <= i; j++){
          if(i % j == 0){
              count++;
          }
      }
      answer += count % 2 == 0 ? i : -i;
  }
  
  return answer;
}