while True:
    n = int(input())
    if n == 0: break
    pa, pb = 0, 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b: pa+=1
        elif b > a: pb+=1
    print(pa, pb)