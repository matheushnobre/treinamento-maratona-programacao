def f(p):
    fib = [1, 2]
    if p in [1, 2, 3]:
        return p
    for i in range(p-2):
        fib.append(fib[-1] + fib[-2])
    return fib[-1]

while True:
    n = int(input())
    if n == 0: break
    print(f(n))