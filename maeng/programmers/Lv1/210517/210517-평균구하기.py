# https://programmers.co.kr/learn/courses/30/lessons/12944?language=python3

def solution(arr):
    answer = 0
    for a in arr:
        answer += a
    return answer/len(arr)

if __name__ == "__main__":
    arr = [1,2,3,4]
    print(solution(arr))
