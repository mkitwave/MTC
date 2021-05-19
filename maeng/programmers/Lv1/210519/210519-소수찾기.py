# https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3

# 1 ~ n 사이의 소수 개수 반환
# 소수 != 1 and 자기자신 또는 1 % n == 0
# 예: n = 10 => [2,3,5,7] 4개 존재. return 4

def solution(n):
    num = set(range(2, n+1))            # {2, 3, 4, 5, 6, 7, 8, 9, 10}
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))      # 2*i부터 n+1까지, 간격은 i만큼 / i가 2일경우 4, 10(포함), 2
    return len(num)

if __name__ == '__main__':
    n = 10
    print(solution(n))