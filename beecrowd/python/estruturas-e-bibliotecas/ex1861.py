contagem = {}
mortos = []
while True:
    try:
        assassino, assassinado = input().split()
        mortos.append(assassinado)
        try:
            contagem[assassino] += 1
        except KeyError:
            contagem[assassino] = 1
    except EOFError:
        for morto in mortos:
            try:
                del contagem[morto]
            except KeyError:
                continue
        saida = sorted(contagem.items(), key=lambda x:x[0])
        print('HALL OF MURDERERS')
        for v in saida:
            print(v[0], v[1], sep=' ')
        break