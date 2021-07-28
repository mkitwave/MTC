// https://programmers.co.kr/learn/courses/30/lessons/12930
function solution(s) {
  return s.split(' ').map(word =>{
      let answer = '';     
      for(var i=0; i<word.length; i++){
          answer += (i % 2 === 0) ? word[i].toUpperCase() : word[i].toLowerCase();
      }
      return answer;
  }).join(' ');
}