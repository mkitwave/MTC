# 프로그래머스 | N개의 최소공배수(https://programmers.co.kr/learn/courses/30/lessons/12953)

def lcm(a, b):
    if a < b:
        max = b
    else:
        max = a
    for i in range(max, (a * b) + 1):
        if i % a == 0 and i % b == 0:
            res = i
            break
    return res

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    answer = arr[0]
    for i, a in enumerate(arr):
        answer = lcm(answer, arr[i + 1])
        if i == len(arr) - 2:
            return answer