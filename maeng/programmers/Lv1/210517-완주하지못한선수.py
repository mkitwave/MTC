# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant, completion = sorted(participant), sorted(completion)
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))