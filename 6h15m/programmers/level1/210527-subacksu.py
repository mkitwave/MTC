# 프로그래머스 | 수박수박수박수박수박수? (https://programmers.co.kr/learn/courses/30/lessons/12922)

def solution(n):
    wm = ['수', '박']
    return ''.join([wm[i % 2] for i in range(n)])