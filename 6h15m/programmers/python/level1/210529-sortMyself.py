# 프로그래머스 | 문자열 내 마음대로 정렬하기 (https://programmers.co.kr/learn/courses/30/lessons/12915)

def solution(s, n):
    return sorted(sorted(s), key=lambda s:s[n])