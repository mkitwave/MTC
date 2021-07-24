// 프로그래머스 | 문자열 내 p와 y의 개수 (https://programmers.co.kr/learn/courses/30/lessons/12916)

function solution(s) {
    let count = 0;
    for (let i of s.toLowerCase()) {
        if (i == 'p') count++;
        if (i == 'y') count--;
    }

    return count == 0;
}