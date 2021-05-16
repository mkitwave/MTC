# https://programmers.co.kr/learn/courses/4008/lessons/66568

import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    m = 1
    for number in numbers:
        m *= number
        if math.sqrt(m) == int(math.sqrt(m)):
            print('found')
            break
    else: print('not found')