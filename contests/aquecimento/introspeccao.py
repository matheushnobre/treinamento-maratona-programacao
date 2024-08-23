dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
indexs = {v : [] for v in dic.values()}

lista = input()
for i, c in enumerate(lista):
    v = dic[c]
    indexs[v].append(i)

maior = 0
intervalos = []

for i in range(16):
    listaI = indexs[i]
    for possibilidade in listaI:
        tam = 1
        inicio = possibilidade
        ultimo = inicio
        for j in range(i+1, 16):
            listaJ = indexs[j]
            parou = True
            for continuando in listaJ:
                if continuando > ultimo:
                    ultimo = continuando
                    tam += 1
                    parou = False
                    break
            if parou:
                if tam == maior:
                    intervalos.append((inicio, ultimo))
                elif tam > maior:
                    maior = tam
                    intervalos = [(inicio, ultimo)]
                break
        if tam == maior:
            intervalos.append((inicio, ultimo))
        elif tam > maior:
            maior = tam
            intervalos = [(inicio, ultimo)]

if tam == maior:
    intervalos.append((inicio, ultimo))
elif tam > maior:
    maior = tam
    intervalos = [(inicio, ultimo)]
            
if maior < 3:
    print('NAO EXISTE')
else:
    razao = None
    for int in intervalos:
        tamanho = int[1]-int[0]
        if razao == None: razao = maior/tamanho
        else: razao = min(razao, maior/tamanho)
    print(f'{maior} {razao:.2f}')