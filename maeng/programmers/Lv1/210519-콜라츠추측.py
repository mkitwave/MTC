# https://programmers.co.kr/learn/courses/30/lessons/12943

'''
1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
'''

# 500번 시도했을 때 1이 되지 못하면 -1 리턴
# num이 1이 되지 않을때에만 반복
# 1이 되면 return

def solution(num):
    for i in range(500+1):
        if num!=1:
            if num%2==0:
                num = num//2
            else:
                num = num*3+1
        else:
            answer = i
            return answer
    return -1

if __name__ == '__main__':
    num = 16
    print(solution(num))