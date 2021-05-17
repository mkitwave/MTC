# https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    length = len(s)
    if length % 2 != 0:
        length //= 2
        return s[length]
    else:
        length //= 2
        return s[length-1]+s[length]

if __name__ == '__main__':
    s = "abcde"
    print(solution(s))