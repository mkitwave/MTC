// https://programmers.co.kr/learn/courses/30/lessons/12933

function solution(n) { 
  //string 변환 -> string 자르기 -> string 내림자춘 정렬 -> 배열 합치기
  return parseInt(String(n).split('').sort((a,b) => b - a).join('')); 
}
