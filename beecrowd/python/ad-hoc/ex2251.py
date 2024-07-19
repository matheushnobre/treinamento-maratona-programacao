def hanoi(n):
    if n==1:
        return 1
    else:
        return 2*hanoi(n-1)+1

ct=0
while True:
    ct+=1
    n = int(input())
    if n==0: break
    print(f'Teste {ct}')
    print(hanoi(n))
    print()
