# https://programmers.co.kr/learn/courses/4008/lessons/13339

def solution(mylist):
    new_list = list(map(list, zip(*mylist)))
    return new_list


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
