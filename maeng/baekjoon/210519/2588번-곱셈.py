# https://www.acmicpc.net/problem/2588

n1 = int(input())
n2 = input()

for i in range(0, 3):
    result = n1 * int(n2[2-i])
    print(result)
print(n1*int(n2))
