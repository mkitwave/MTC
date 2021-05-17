# 백준 1924번 | 2007년 (https://www.acmicpc.net/problem/1924)
answer = ''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
m, d = input().split()
m = int(m)
d = int(d)
for i in range(m - 1):
    d += months[i]
print(days[d % 7 - 1])