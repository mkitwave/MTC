answer = [] #m개의 수열을 저장하기 위한 리스트

def sol():
  if len(answer) == m:  #리스트에 들어간 수열이 m개이면 함수 빠져나옴.
    print(' '.join(map(str, answer))) #리스트에 들어있는 숫자 출력
    return

  for i in range(1, n + 1):
    if i in answer: #리스트가 중복인 경우 continue
      continue
    answer.append(i)  #수열 추가
    sol() #다음 숫자를 넣기 위한 가지치기
    answer.pop()  #수열 마지막 자리 삭제

n, m = map(int, input().split())
sol()