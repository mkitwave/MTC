# https://programmers.co.kr/learn/courses/30/lessons/12933?language=python3

def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))

if __name__ == '__main__':
    n = 118372
    print(solution(n))

n = 118372
print(list(str(n)))