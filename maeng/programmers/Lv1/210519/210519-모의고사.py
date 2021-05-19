# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

# 반복문으로 하나씩 돌려서 numN[i]와 answer[i] 비교
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬

def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):          # 튜플 형태로 반환
        if answer == num1[idx%len(num1)]:
            score[0] += 1
        if answer == num2[idx%len(num2)]:
            score[1] += 1
        if answer == num3[idx%len(num3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

if __name__ == '__main__':
    answers = [1,3,2,4,2]
    print(solution(answers))