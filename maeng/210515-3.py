# https://programmers.co.kr/learn/courses/4008/lessons/13168

num, base = map(int, input().strip().split(' '))
result = 0
for i in range(len(str(num))):
    result += int(str(num)[-1-i]) * (base**i)
print(result)

# 다른 풀이
num = '3212'
base = 5
answer = int(num, base)
print(answer)