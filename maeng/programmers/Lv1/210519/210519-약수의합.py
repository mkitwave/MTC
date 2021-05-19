# https://programmers.co.kr/learn/courses/30/lessons/12928?language=python3

def solution(n):
    answer = 0
    for i in range(1, n+1):         # 1부터 n까지
        if n%i == 0:
            answer+=i
    return answer

if __name__ == '__main__':
    n = 5
    print(solution(n))