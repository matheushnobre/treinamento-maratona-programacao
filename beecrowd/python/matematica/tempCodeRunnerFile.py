fibo = [0, 1]
while len(fibo) < 10001:
    fibo.append(fibo[-1]+fibo[-2])

n = int(input())

for i in range(n):
    num = int(input(), 2)
    ans = fibo[num]
    print('{:03d}'.format(ans))