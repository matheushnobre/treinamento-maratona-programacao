while True:
    try:
        entrada = input()
    except EOFError: break
    
    saida = ''
    aux = ''
    isHome = False
    
    for c in entrada:
        if c == '[':
            saida = aux + saida
            aux = ''
            isHome = True
        elif c == ']':
            saida = aux + saida
            aux = ''
            isHome = False
        else:
            if isHome: aux += c
            else: saida += c
          
    saida = aux + saida      
    print(saida)