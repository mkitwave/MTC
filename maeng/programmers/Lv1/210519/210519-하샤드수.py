# https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

# 하샤드 수 : x의 자릿수의 합으로 x가 나누어지는 수
# 예 : 18 => 1 + 8 = 9, 18 % 9 == 0

# 입력받은 수를 리스트화 해서 잘게 쪼개기
# 쪼갠 숫자들을 더함
# 더한 것을 입력받은 수 와 나눔. 0일 경우 True / 그 외의 수 False

def solution(x):
    x_slice = list(map(int, str(x)))      # x가 10일 경우 [1, 0]
    if x % sum(x_slice) == 0:
        return True
    return False

if __name__ == '__main__':
    x = 10
    print(solution(x))