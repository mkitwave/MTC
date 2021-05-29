# 프로그래머스 | 최대공약수와 최소공배수 (https://programmers.co.kr/learn/courses/30/lessons/12940)

import math as t
def solution(n, m):
    return [t.gcd(n, m), (n*m)/t.gcd(n, m)]