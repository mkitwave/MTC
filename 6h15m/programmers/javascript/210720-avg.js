// 프로그래머스 | 평균 구하기 (https://programmers.co.kr/learn/courses/30/lessons/12944)

function solution(arr) {
    return (arr.reduce((prev, curr) => prev + curr, 0) / arr.length);
}