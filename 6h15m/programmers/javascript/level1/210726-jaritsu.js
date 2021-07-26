// 프로그래머스 | 자릿수 더하기 (https://programmers.co.kr/learn/courses/30/lessons/12931)

function solution(n) {
  return String(n)
    .split("")
    .map((x) => x * 1)
    .reduce((a, b) => a + b);
}
