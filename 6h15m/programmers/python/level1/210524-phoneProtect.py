# 프로그래머스 | 핸드폰 번호 가리기 (https://programmers.co.kr/learn/courses/30/lessons/12948)

def solution(p):
    return '*'*(len(p)-4)+p[len(p)-4:]