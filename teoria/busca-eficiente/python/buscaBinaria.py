# 1ª solução
def busca(vetor, item, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    while inicio <= fim:
        m = (inicio + fim) // 2

        if vetor[m] == item:
            return m
        elif vetor[m] < item:
            inicio = m + 1
        else:
            fim = m - 1
    return -1

vetor = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(busca(vetor, 13))  # Saída esperada: 6

# Solução recursiva
def busca(vetor, item, inicio=0, fim=None):
    if fim is None:
        fim = len(vetor) - 1

    if inicio <= fim:
        m = (inicio + fim) // 2
        if vetor[m] == item:
            return m
        elif item < vetor[m]:
            return busca(vetor, item, inicio, m - 1)
        else:
            return busca(vetor, item, m + 1, fim)
    return -1

vetor = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(busca(vetor, 13))  # Saída esperada: 6
