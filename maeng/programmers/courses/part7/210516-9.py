# https://programmers.co.kr/learn/courses/4008/lessons/48463

def solution(mylist):
    answer = []
    for i in mylist:
        if i % 2 == 0:
            answer.append(i**2)
        else: continue
    return answer

if __name__ == '__main__':
    mylist = [3,2,6,7]
    print(solution(mylist))


# 다른 방법
def solution1(mylist):
    answer = [i**2 for i in mylist if i % 2 == 0]
    return answer

if __name__ == '__main__':
    mylist = [3,2,6,7]
    print(solution1(mylist))