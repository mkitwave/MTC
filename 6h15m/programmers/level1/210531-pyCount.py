# 프로그래머스 | 문자열 내 p와 y의 개수 (https://programmers.co.kr/learn/courses/30/lessons/12916)

def solution(s):
    p = s.count('p') + s.count('P')
    y = s.count('y') + s.count('Y')
    return p == y and p > 0 and y > 0