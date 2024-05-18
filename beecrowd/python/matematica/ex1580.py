from math import factorial

while True:
    try:
        palavra, letras = input(), []
        repetidas = 1

        for l in palavra:
            if l not in letras:
                repetidas *= factorial(palavra.count(l))
                letras.append(l)
        
        perm = factorial(len(palavra)) // repetidas
        print(perm  % 1000000007)
    except EOFError:
        break