# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    answer = ''
    num = ['1', '2', '4']
    while n > 0:
        n -= 1
        answer = num[n%3] + answer
        n //= 3
    return answer

if __name__ == '__main__':
    n = 1
    print(solution(n))