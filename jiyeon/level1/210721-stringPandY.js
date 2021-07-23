// https://programmers.co.kr/learn/courses/30/lessons/12916
function solution(s){
  var answer = true;
  var str = s.toUpperCase().split('');
  var count_P = 0;
  var count_Y = 0;
  
  for(var i = 0; i <= str.length; i++){
      if(str[i] == "P") count_P++;
      if(str[i] == "Y") count_Y++;
  }
  
  if (count_P == count_Y) return answer;
  else return false;
}