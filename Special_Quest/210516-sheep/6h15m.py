# 난이도 조절 실패한 특별 문제
# 깊이우선탐색(DFS)과 재귀호출에 대한 이해도를 쌓고 재도전할 것!

def solution(h, w, arr):
    answer = 0

    return answer


answers = []
n = int(input())

for i in range(0, n):
    h, w = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(h)]
    answers.append(solution(h, w, arr))

for a in answers:
    print(a)

'''
예제 복사용
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###

참고 블로그
https://wave1994.tistory.com/115
https://minjoos.tistory.com/2
'''