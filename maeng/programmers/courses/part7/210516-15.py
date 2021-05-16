# https://programmers.co.kr/learn/courses/4008/lessons/13317

if __name__ == '__main__':
    f = open('myfile.txt', 'r')
    while True:
        line = f.readline()
        if not line:
            break
        raw = line.split()
        print(raw)
    f.close()

print()

'''
다른 방법 (with-as 구문 사용)
장점 : 1) with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
      2) readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다. 
      3) with - as 구문은 파일 뿐만 아니라 socket이나 http 등에서도 사용할 수 있습니다.
'''
if __name__ == '__main__':
    with open('myfile.txt') as file:
        for line in file.readlines():
            print(line.strip().split('\t'))