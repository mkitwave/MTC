# 프로그래머스 | 전화번호 목록 (https://programmers.co.kr/learn/courses/30/lessons/42577)

def solution(phone_book):
    phone_book.sort()
    for i, p in enumerate(phone_book):
        if i < len(phone_book) - 1:
            i = phone_book[i + 1]
        else: return True
        if i.startswith(p):
            return False
    return True