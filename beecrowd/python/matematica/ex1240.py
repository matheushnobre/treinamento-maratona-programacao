n = int(input())

for i in range(n):
    a, b = input().split()
    if len(b) > len(a): 
        print('nao encaixa')
    else:
        if a[len(a)-len(b):] == b:
            print('encaixa')
        else:
            print('nao encaixa')