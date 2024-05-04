q, i, g, e = 0, 0, 0, 0
while True:
    q += 1
    gi, gg = map(int, input().split())
    
    if gi > gg:
        i += 1
    elif gi == gg:
        e += 1
    else:
        g += 1
        
    c = input('Novo grenal (1-sim 2-nao)\n')
    if c == '2': break
    
print(f'{q} grenais')
print(f'Inter:{i}') 
print(f'Gremio:{g}')
print(f'Empates:{e}')

if i > g:
    print('Inter venceu mais')
elif g > i:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')