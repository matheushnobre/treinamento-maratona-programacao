palavras = set()

while True:
    try:
        linha = input().lower()
        pal = ''
        for c in linha:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                if pal == '': pal = c
                else: pal += c
            else:
                palavras.add(pal)
                pal = ''
        palavras.add(pal)
        
    except EOFError:
        palavras = list(palavras)
        palavras.sort()
        if '' in palavras:
            del palavras[0]
        print(*palavras, sep='\n')
        break