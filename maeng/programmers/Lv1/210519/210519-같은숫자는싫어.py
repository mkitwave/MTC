# https://programmers.co.kr/learn/courses/30/lessons/12906?language=python3

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

if __name__ == "__main__":
    arr = [4,4,4,3,3]
    print(solution(arr))