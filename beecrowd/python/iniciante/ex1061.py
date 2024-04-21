d0 = int(input().split()[1]) 
h0, m0, s0 = map(int, input().split(' : ')) 
df = int(input().split()[1]) 
hf, mf, sf = map(int, input().split(' : ')) 

s, m, h, d = 0, 0, 0, 0 # inicializa as variáveis responsáveis pela saída e as declara como 0
if sf>=s0: # verifica se o segundo final é maior que o inicial
    s = sf-s0 # calcula o segundo da saída
else: # se o final for menor que o inicial, este bloco será executado
    s = 60-abs(sf-s0) # o resultado da saída será o módulo da subtração do segundo final pelo segundo inicial
    m = -1 # o valor do minuto será decrementado em 1

# a mesma lógica serve para as variáveis de minuto hora 
if mf>=m0:
    m += mf-m0
else:
    m += 60-abs(mf-m0)
    h = -1

if hf>=h0:
    h += hf-h0
else: 
    h += 24-abs(hf-h0)
    d = -1
    
# verifica se o minuto ou a hora ficaram negativos. caso tenha ocorrido, faz as correções
if m == -1:
    h -= 1
    m = 59
elif h == -1:
    d -= 1
    h = 23
    
d += df - d0
print(f'{d} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)')