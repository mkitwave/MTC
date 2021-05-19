# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    def strings_sortkey(x):
        return x[n]
    return sorted(sorted(strings), key=strings_sortkey)

if __name__ == '__main__':
    strings = ["abce", "abcd", "cdx"]
    n = 2
    print(solution(strings, n))