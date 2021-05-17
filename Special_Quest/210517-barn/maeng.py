if __name__ == '__main__':
    n, w, h, l = map(int, input().strip().split())
    if (w//l)*(h//l) >= n : print(n)
    else: print((w//l)*(h//l))