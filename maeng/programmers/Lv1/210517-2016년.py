# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

from datetime import datetime
def solution(a, b):
    days = 'MON TUE WED THU FRI SAT SUN'.split()
    return days[datetime(2016, a, b).weekday()]

if __name__ == '__main__':
    a, b = 5, 24
    print(solution(a, b))