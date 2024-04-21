a = [c for c in input() if c.isdigit() or c == '.']
newA = ''
for c in a:
    newA += c
    
b = [c for c in input() if c.isdigit() or c == '.']
newB = ''
for c in b:
    newB += c
        
if '.' in newA: newA = newA[:(newA.index('.')+3)]
if '.' in newB: newB = newB[:(newB.index('.')+3)]
        
cpf = newA[:11]
valA, valB = float(newA[11:]), float(newB)
soma = valA + valB

print('cpf', cpf)
print(f'{soma:.2f}')