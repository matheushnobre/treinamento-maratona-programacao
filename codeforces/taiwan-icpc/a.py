others = [] # Vetor pra armazenar os animais que não são porcos
pig = 0 # Variável pra armazenar o porco de maior influência
n = int(input())

for _ in range(n):
    a, i = input().split()
    if a == 'pig':
        pig = max(pig, int(i))
    else:
        others.append(int(i))
        
answer = pig # Iniciamos a resposta com o valor do porco de menor influência
for v in others:
    if v < pig: answer += v # Adicionamos ao grupo todos os animais que possuem influência menor
    
print(answer)