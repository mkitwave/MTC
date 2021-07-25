// 프로그래머스 | 콜라츠 추측 (https://programmers.co.kr/learn/courses/30/lessons/12943)

let count = 0;
function solution(num) {
    if (num == 1) return count;
    count++;
    if (count == 500) return -1;

    return solution((num % 2) ? num * 3 + 1 : num / 2);
}