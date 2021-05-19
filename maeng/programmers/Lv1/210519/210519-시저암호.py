# https://programmers.co.kr/learn/courses/30/lessons/12926?language=python3

import string

def solution(s, n):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    result = ""

    for char in s:
        if char == " ":                 # 공백 추가
            result += char
        elif char in lowers:
            result += lowers[(lowers.index(char) + n) % 26]     # char 위치 찾은 후 n 만큼 이동
        else:
            result += uppers[(uppers.index(char) + n) % 26]     # 알파벳 개수: 26

    return result

if __name__ == '__main__':
    s = "AB"
    n = 1
    print(solution(s, n))