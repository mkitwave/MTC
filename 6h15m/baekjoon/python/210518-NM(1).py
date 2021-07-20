from itertools import permutations as p
n,m=map(int,input().split())
s = p(range(1, n+1), m)
for i in s:
    print(' '.join(map(str, i)))