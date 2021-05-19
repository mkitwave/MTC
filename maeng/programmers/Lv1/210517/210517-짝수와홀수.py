# https://programmers.co.kr/learn/courses/30/lessons/12937?language=python3

def solution(num):
    if num % 2 == 0: return "Even"
    else: return "Odd"

if __name__ == "__main__":
    num = 3
    print(solution(num))