// https://programmers.co.kr/learn/courses/30/lessons/12906

function solution(arr) {
  return arr.filter((num, index) => num !== arr[index+1]);
}