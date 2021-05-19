# https://programmers.co.kr/learn/courses/30/lessons/12940?language=python3

def solution(n, m):
    answer = gcd(max(n,m), min(n,m))
    return [answer, int((n*m)/answer)]      #최대공약수, 최소공배수

def gcd(n, m):
    while m > 0:
        tmp = m
        m = n%m                 # 3%12 => 3
        n = tmp
    return n

if __name__ == '__main__':
    n, m = 3, 12
    print(solution(n, m))