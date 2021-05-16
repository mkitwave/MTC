# https://programmers.co.kr/learn/courses/4008/lessons/13328

def solution(mylist):
    return list(map(int, mylist))

if __name__ == '__main__':
    mylist = ['1', '100', '33']
    print(solution(mylist))