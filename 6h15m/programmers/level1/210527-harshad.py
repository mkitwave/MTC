# 프로그래머스 | 하샤드 수 (https://programmers.co.kr/learn/courses/30/lessons/12947)

def solution(x):
    return not bool(x % sum(map(int, str(x))))