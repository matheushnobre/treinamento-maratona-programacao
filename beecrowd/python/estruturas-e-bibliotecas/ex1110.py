def realocar(cartas):
    last = [cartas.pop()]
    last.extend(cartas)
    return last

while True:
    n = int(input())
    if n == 0: break
    
    cartas = [i for i in range(1, n+1)]
    cartas.reverse()
    
    saida = 'Discarded cards: '
    while len(cartas) > 1:
        if len(cartas) > 2: saida += f'{cartas.pop()}, ' 
        else: saida += str(cartas.pop())
        cartas = realocar(cartas)
    saida += f'\nRemaining card: {cartas.pop()}'
    print(saida)