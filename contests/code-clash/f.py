t = int(input())
for i in range(t):
    n = int(input())
    lista = list(map(int, input().split()))
    lista.sort(reverse=True)
    
    answer = 0
    for i in range(2, n, 3):
        answer += lista[i]
        
    print(answer)
    