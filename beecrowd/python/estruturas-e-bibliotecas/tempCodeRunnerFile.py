palavras = set()

while True:
    try:
        linha = input().lower()
        pal = ''
        for c in linha:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                pal += c
            else:
                palavras.add(pal)
                pal = ''
        if pal != '':
            palavras.add(pal)
            
    except EOFError:
        palavras = list(palavras)
        palavras.sort()
        if len(palavras) > 5000:
            palavras = palavras[:5000]
        print(*palavras, sep='\n')
        break