# https://programmers.co.kr/learn/courses/4008/lessons/13173
# 이진 탐색 - 오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘. 검색 속도가 아주 빠름

import bisect

if __name__ == '__main__':
    mylist = list(map(int, input().strip().split(' ')))
    print(bisect.bisect(mylist, 3))