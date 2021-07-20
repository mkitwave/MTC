#프로그래머스 | 더 맵게 (https://programmers.co.kr/learn/courses/30/lessons/42626)
import heapq

def solution(scoville, K):
    result = 0
    heapq.heapify(scoville)
    while(scoville):
        if (len(scoville) == 2):
            if(scoville[0] + (scoville[1] * 2) < K):
                return -1
        min_1 = heapq.heappop(scoville)
        if min_1 >= K:
            return result
        else:
            min_2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min_1 + (min_2 * 2))
            result += 1
    