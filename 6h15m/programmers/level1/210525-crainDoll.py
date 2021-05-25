# 프로그래머스 | 크레인 인형뽑기 게임 (https://programmers.co.kr/learn/courses/30/lessons/64061)

def solution(board, moves):
    basket = []
    answer = 0
    doll = 0
    for m in moves:
        for i in range(len(board)):
            c = m - 1
            if (board[i][c] != 0):
                doll = board[i][c]
                board[i][c] = 0
                if len(basket) == 0:
                    basket.append(doll)
                elif len(basket) > 0 and doll != basket[-1]:
                    basket.append(doll)
                else:
                    answer += 1
                    del basket[-1]
                break
    return answer * 2