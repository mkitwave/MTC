# https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

def solution(s):
    return len(s) in(4, 6) and s.isdigit()

if __name__ == '__main__':
    s = 'a234'
    print(solution(s))