# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

#s에서 공백이 있는 인덱스를 저장 후 공백제거, 변환한 문자에 공백 추가
def solution(s):
    answer = []
    s = s.split(" ")
    print(s)
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                answer.append(s[i][j].upper())
            else:
                answer.append(s[i][j].lower())
        answer.append(" ")

    answer = ''.join(answer)
    answer = answer[0:len(answer)-1]
    return answer

if __name__ == '__main__':
    s = "try hello world"
    print(solution(s))