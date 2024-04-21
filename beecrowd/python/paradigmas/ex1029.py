def fibo(n):
    f = [0, 1, 1]
    c = [0, 0, 2]
    for i in range(n-2):
        f.append(f[-1] + f[-2])
        c.append(c[-1]*2 - c[-3])
    return c[n], f[n]
    
t = int(input())
for i in range(t):
    n = int(input())
    c, f = fibo(n)
    print(f'fib({n}) = {c} calls = {f}')