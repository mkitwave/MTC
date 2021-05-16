# https://programmers.co.kr/learn/courses/4008/lessons/13246

import collections

if __name__ == '__main__':
    my_str = input().strip()
    my_str = sorted(my_str)
    cnt = collections.Counter(my_str)
    cnt = cnt.most_common()             # 입력된게 'aab'일 경우 [('a',2), ('b',1)] 형태로 보여줌
    collect = []

    for i in range(0, len(cnt)):
        if cnt[i][1] == cnt[0][1]:
            collect.append(cnt[i][0])
    print(''.join(collect))
