# O bubble sort realiza múltiplas passagem por uma lista
# Ele compara itens adjacentes e troca aqueles que estão fora de ordem
# Complexidade: O(n^2)

def bubbleSort(lista):
    for passnum in range(len(lista)-1, 0, -1):
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                
lista = [54,26,93,17,77,31,44,55,20]
bubbleSort(lista)
print(lista)