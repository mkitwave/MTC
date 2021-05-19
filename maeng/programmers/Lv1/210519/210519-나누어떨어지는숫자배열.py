# https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3

def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

if __name__ == '__main__':
    arr = [2, 36, 1, 3]
    divisor = 1
    print(solution(arr, divisor))