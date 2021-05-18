# https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    return f'김서방은 {seoul.index("Kim")}에 있다'

if __name__ == "__main__":
    seoul = ["Jane", "Kim"]
    print(solution(seoul))