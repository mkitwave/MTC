# https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3

if __name__ == '__main__':
    a, b = map(int, input().strip().split(' '))
    print(('*' * a + '\n')*b)