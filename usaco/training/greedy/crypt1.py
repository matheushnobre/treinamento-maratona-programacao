'''
ID: matheus30
TASK: crypt1
LANG: PYTHON3               
'''         

def combinarN1(numbers):
    lista = []
    for a in numbers:
        for b in numbers:
            for c in numbers:
                n = int(a+b+c)
                lista.append(n)
    return lista

def combinarN2(numbers):
    lista = []
    for a in numbers:
        for b in numbers:
            n = int(a+b)
            lista.append(n)
    return lista


fin = open('crypt1.in', 'r')
fout = open('crypt1.out', 'w')

n = int(fin.readline())
numbers = fin.readline().split()
numbers.sort()
a = combinarN1(numbers)
b = combinarN2(numbers)

s = 0
for n1 in a:
    for n2 in b:
        mult = str(n1*n2)
        if len(mult) > 4:
            break

        ehSolucao = True
        p1 = str(n1 * int(str(n2)[1]))
        p2 = str(n1 * int(str(n2)[0]))
        if len(p1) != 3 or len(p2) != 3 or len(mult) != 4: 
            continue
        
        for v in mult:
            if v not in numbers:
                ehSolucao = False
                break
        for v in p1:
            if v not in numbers:
                ehSolucao = False
                break
        for v in p2:
            if v not in numbers:
                ehSolucao = False
                break
        if ehSolucao: 
            s+=1
        
fout.write(f'{s}\n')