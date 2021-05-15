#프로그래머스 | 피보나치 수 (https://programmers.co.kr/learn/courses/30/lessons/12945)
'''
첫번째 실패 - 런타임 에러로 오답 발생
def solution(n):
    if n == 0 or n == 1:
        return n
    n = solution(n-1) + solution(n-2)
    return n % 1234567
'''

'''
두번째 실패 - 런타임 에러로 오답 발생
def solution(n):
    if n == 0 or n == 1:
        return n
    n = n * 1234567 + (solution((n-1) % 1234567) + solution((n-2) % 1234567))
    return n % 1234567
'''

'''
세번째 실패 - 런타임 에러로 오답 발생
def solution(n):
    if n == 0 or n == 1:
        return n
    n = (solution(n-1) + solution(n-2)) % 1234567
    return n
'''

'''
네번째 실패 - 런타임 에러로 오답 발생
def solution(n):
    if n == 0 or n == 1:
        return n
    n = ((solution(n-1) % 1234567) + (solution(n-2) % 1234567)) % 1234567 
    return n
'''

# 재귀함수 버리고 광명찾기
def solution(n):
    a, b = 0, 1
    if n < 2:
        return n
    for i in range(2, n + 1):
        a, b = b, a + b
    return b % 1234567

# 다른 사람의 풀이(천재)
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a