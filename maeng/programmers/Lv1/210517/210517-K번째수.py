# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

if __name__ == '__main__':
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array, commands))