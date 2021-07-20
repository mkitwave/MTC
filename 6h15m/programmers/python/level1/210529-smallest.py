# 프로그래머스 | 제일 작은 수 제거하기 (https://programmers.co.kr/learn/courses/30/lessons/12935)

def solution(a):
    a.remove(min(a))
    return [-1] if len(a) == 0 else a