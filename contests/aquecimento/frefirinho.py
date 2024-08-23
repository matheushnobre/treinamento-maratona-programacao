import sys

a, p, j = map(int, input().split())
torre = [p for i in range(a)]
jogador = 0

input = sys.stdin.read()
entrada = input.split()

perdeu = False
for num in entrada:
    n = int(num)
    jogador += 1
    if jogador == j+1: jogador = 1
    
    torre[n-1] -= 1
    if torre[n-1] == 0:
        print(jogador)
        perdeu = True
        break
    
    elif n < a and torre[n-1] == 1 and torre[n] == 1: 
        print(jogador)
        perdeu = True
        break
    
if not perdeu:
    print(-1)
    
