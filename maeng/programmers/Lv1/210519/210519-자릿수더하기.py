# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3

def solution(n):
    # n을 분리하고 다 더하기. (sum)
    return sum(list(map(int, str(n))))

if __name__ == '__main__':
    n = 987
    print(solution(n))