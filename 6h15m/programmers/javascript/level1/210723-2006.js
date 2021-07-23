// 프로그래머스 | 2016년 (https://programmers.co.kr/learn/courses/30/lessons/12901)

function solution(a, b) {
    const months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];

    for (let i = 0; i < a - 1; i++) {
        b += months[i];
    }

    return days[b % 7];
}