// 프로그래머스 | 가운데 글자 가져오기 (https://programmers.co.kr/learn/courses/30/lessons/12903)

function solution(s) {
  return s.length % 2 ? s[(s.length - 1) / 2] : s.substr(s.length / 2 - 1, 2);
}
