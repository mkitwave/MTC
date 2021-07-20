# 프로그래머스 | 완주하지 못한 선수 (https://programmers.co.kr/learn/courses/30/lessons/42576)

def solution(participant, completion):
    answer = ''
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
    for p in participant:
        if dic[p] == 1:
            answer = p
    return answer