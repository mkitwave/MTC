# https://programmers.co.kr/learn/courses/30/lessons/12934?language=python3

def solution(n):
    sqrt = n**(1/2)
    if sqrt % 1 == 0:
        return int(sqrt+1)**2
    return -1

if __name__ == '__main__':
    n = 121
    print(solution(n))