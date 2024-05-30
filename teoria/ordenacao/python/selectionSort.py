# A ordenação por seleção melhora o bubble sort ao realizar apenas uma troca a cada passagem pela lista.
# A ordenação por seleção procura pelo valor mais alto enquanto faz uma passagem e, depois de completá-la, coloca-o na posição correta.
# Complexidade: O(n^2)

def selectionSort(lista):
    for i in range(len(lista)-1, 0, -1):
        indexMaior = 0
        for j in range(1, i+1):
            if lista[j] > lista[indexMaior]:
                indexMaior = j
        
        lista[j], lista[indexMaior] = lista[indexMaior], lista[j] 

lista = [54,26,93,17,77,31,44,55,20]
selectionSort(lista)
print(lista)
