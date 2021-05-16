# https://programmers.co.kr/learn/courses/4008/lessons/13340

num = int(input().strip())
if num == 0:
    print('abcdefghijklmnopqrstuvwxyz')
else: print('abcdefghijklmnopqrstuvwxyz'.upper())

# 다른 풀이
import string
num = int(input().strip())
if num == 0:
    print(string.ascii_lowercase)
else : print(string.ascii_uppercase)