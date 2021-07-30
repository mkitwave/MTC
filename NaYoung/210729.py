def fact(n):
    arr = [1]*(n+1)
    for i in range(1, n+1):
        arr[i] = arr[i-1]*i
    return arr


def solution(n, k):
    ori = [i for i in range(1, n + 1)]
    fact_list = fact(n)
    result = []
    k = k-1
    while n > 0:
        val1 = k % fact_list[n - 1]
        val2 = k // fact_list[n - 1]
        n = n - 1
        k = val1
        result.append(val2)
    answer = []
    for r in result:
        answer.append(ori.pop(r))
    return answer