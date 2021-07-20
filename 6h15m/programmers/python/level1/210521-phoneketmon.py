# 프로그래머스 | 폰켓몬 (https://programmers.co.kr/learn/courses/30/lessons/1845)
def solution(nums):
    s_nums = set(nums)
    return len(s_nums) if len(s_nums) <= len(nums)/2 else len(nums)/2