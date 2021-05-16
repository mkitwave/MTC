# https://programmers.co.kr/learn/courses/4008/lessons/72546

def solution(mylist):
    answer = []
    for i in range(len(mylist)-1):
        answer.append(abs(mylist[i+1]-mylist[i]))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))


# zip을 사용한 방법
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1-number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]
    print(solution(mylist))