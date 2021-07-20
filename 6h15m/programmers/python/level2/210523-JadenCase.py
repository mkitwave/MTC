# 프로그래머스 | JadenCase 문자열 만들기(https://programmers.co.kr/learn/courses/30/lessons/12951)

def solution(s):
    return ' '.join([w.capitalize() for w in s.split(' ')])