# https://programmers.co.kr/learn/courses/4008/lessons/13347

def solution(mylist):
    mylist = sorted(mylist)
    n = len(mylist)
    used = [0]*n
    res = [0]*n
    answer = []

    def f(k, n):
        if k == n:
            a = []
            for i in res:
                a.append(i)
            answer.append(a)
            return answer
        else:
            for i in range(n):
                if used[i] == 0:
                    used[i] = 1
                    res[k] = mylist[i]
                    f(k+1, n)
                    used[i] = 0
    f(0, n)
    return answer

if __name__ == '__main__':
    mylist = [2, 1]
    print(solution(mylist))