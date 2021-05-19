# https://programmers.co.kr/learn/courses/30/lessons/12935?language=python3

def solution(arr):
    if len(arr) == 0:
        return -1
    else:
        arr.remove(min(arr))
        return arr

if __name__ == '__main__':
    arr =[4,3,2,1]
    print(solution(arr))