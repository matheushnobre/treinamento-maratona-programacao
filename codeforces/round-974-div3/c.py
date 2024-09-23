t = int(input())
for _ in range(t):
    n = int(input())
    riq = list(map(int, input().split()))
    riq.sort()
    
    if n == 1 or n == 2:
        print(-1)
        continue
    
    maior = riq[-1]
    total = sum(riq)
    riqmedia = (total / n) / 2
    
    im = n//2
    valormetade = riq[im]
    
    if riqmedia > valormetade:
        print(0)
    else:
        novoTotal = valormetade * 2 * n + 1
        print(novoTotal - total)