# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
    return answer

if __name__ == '__main__':
    arr1 = [[1, 2], [2, 3]]
    arr2 = [[3, 4], [5, 6]]
    print(solution(arr1, arr2))