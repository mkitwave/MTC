// https://programmers.co.kr/learn/courses/30/lessons/12901

function solution(a, b) {
  var answer = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
  var date = new Date(2016, a - 1, b);
  
  return answer[date.getDay()];
}