# 프로그래머스 | 신규 아이디 추천 (https://programmers.co.kr/learn/courses/30/lessons/72410)

import re

def solution(new_id):
    #1 소문자 치환
    answer = new_id.lower()
    #2 일부 특수문자 제거
    answer = re.sub('[\~\!\@\#\$\%\^\&\*\(\)\=\+\[\{\]\}\:\?\,\<\>\/]', '', answer)
    #3 연속 마침표 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4 양쪽 마침표 제거
    answer = answer.strip('.')
    #5 빈 문자열일 시 "a" 대입
    if (answer == ''):
        answer = 'a'
    #6 16자 이상일 때 첫 15개를 제외한 나머지 문자를 모두 제거, 끝에 위치한 마침표 제거
    if (len(answer) > 15) :
        answer = answer[:15]
    answer = answer.rstrip('.')
    #7 길이가 2자 이하라면 3자가 될 때까지 마지막 문자 반복 추가
    while len(answer) < 3:
        answer = answer + answer[-1]
    return answer