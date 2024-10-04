n, t = map(int, input().split())
num = int('1'*n)

if n == 1 and t == 10:
    print(-1)
else:
    while True:
        if num % t == 0:
            print(num)
            break
        num += 1