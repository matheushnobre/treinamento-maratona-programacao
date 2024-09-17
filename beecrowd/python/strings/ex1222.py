while True:
    try:
        n, l, c = map(int, input().split())
    except EOFError:
        break
    
    palavras = input().split()
    
    linhas = 0
    tamLinha = 0
    for p in palavras:
        if tamLinha + len(p) <= c:
            tamLinha += len(p) + 1
        else:
            linhas += 1
            tamLinha = len(p) + 1
                    
    if tamLinha >= 0:
        linhas += 1
    
    s = linhas / l
    if s % 1 != 0:
        s += 1
    print(int(s))
