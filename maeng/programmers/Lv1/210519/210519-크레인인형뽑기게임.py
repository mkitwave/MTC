# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

# 어렵다...
def solution(board, moves):
    bucket = []
    answer = []
    for move in moves:
        for i in range(len(board)):
            # moves 배열의 값들이 1부터 시작하는 자연수로 되어있기 때문에 move-1
            # 인덱스로 쓰기 위해서는 0~n 형태여야 하기 때문에 -1를 빼줌
            if board[i][move - 1] > 0:
                bucket.append(board[i][move - 1])
                board[i][move - 1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += bucket[-1:]
                    bucket = bucket[:-2]
                break
    return len(answer) * 2

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves))