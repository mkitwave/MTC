# https://programmers.co.kr/learn/courses/30/lessons/12982?language=python3

def solution(d, budget):
    d.sort()
    while budget < sum(d):          # budget이 sum(d)값 보다 클 때 while 종료
        d.pop()                     # 뒤에서 부터 꺼내기
    return len(d)

if __name__ == '__main__':
    d = [1,3,2,5,4]
    budget = 9
    print(solution(d, budget))