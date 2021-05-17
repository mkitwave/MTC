# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

def solution(s):
    return ''.join(sorted(list(s), reverse=True))

if __name__ == '__main__':
    s = "Zbcdefg"
    print(solution(s))