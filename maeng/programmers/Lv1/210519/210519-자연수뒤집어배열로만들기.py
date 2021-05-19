# https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3

def solution(n):
    return list(map(int, reversed(str(n))))

if __name__ == '__main__':
    n = 12345
    print(solution(n))