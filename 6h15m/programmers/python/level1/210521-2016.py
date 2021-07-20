# 프로그래머스 | 2016년
def solution(a, b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    for i in range(a - 1):
        b += months[i]
    return days[b % 7 - 4]