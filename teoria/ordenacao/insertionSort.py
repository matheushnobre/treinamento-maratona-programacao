# A ordenação por inserção sempre mantém uma sublista ordenada nas posições inferiores da lista
# Cada novo item é "inserido" na sublista anterior de modo que a sublista ordenada fique com um item a mais
# Complexidade: O(n^2)

def insertionSort(lista):
    for index in range(1, len(lista)):
        valorAtual = lista[index]
        posicao = index
        
        while posicao > 0 and lista[posicao-1] > valorAtual:
            lista[posicao] = lista[posicao-1]
            posicao -= 1
        
        lista[posicao] = valorAtual
        
lista = [54,26,93,17,77,31,44,55,20]
insertionSort(lista)
print(lista) 