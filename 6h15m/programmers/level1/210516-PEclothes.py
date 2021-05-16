#프로그래머스 | 체육복 (https://programmers.co.kr/learn/courses/30/lessons/42862)
def solution(n, lost, reserve):
    temp = 0
    lost.sort()
    reserve.sort()
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            temp += 1
        elif l - 1 in reserve:
            if l - 1 in lost:
                continue
            reserve.remove(l - 1)
            temp += 1
        elif l + 1 in reserve:
            if l + 1 in lost:
                continue
            reserve.remove(l + 1)
            temp += 1
            
    return n - (len(lost) - temp)