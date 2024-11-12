class Node:
    def __init__(self, valor):
        self.valor = valor
        self.right = None
        self.left = None
        
def adicionar(valor, no):
    if no is None:
        return Node(valor)
    if valor < no.valor:
        no.left = adicionar(valor, no.left)
    else:
        no.right = adicionar(valor, no.right)
    return no

def posfixa(no, resultado):
    if no is None:
        return
    posfixa(no.left, resultado)
    posfixa(no.right, resultado)
    resultado.append(str(no.valor))
        
def prefixa(no, resultado):
    if no is None:
        return
    resultado.append(str(no.valor))
    prefixa(no.left, resultado)
    prefixa(no.right, resultado)
        
def infixa(no, resultado):
    if no is None:
        return
    infixa(no.left, resultado)
    resultado.append(str(no.valor))
    infixa(no.right, resultado)
    
def main():
    t = int(input())
    for ct in range(t):
        n = int(input())
        no = None
        lista = list(map(int, input().split()))
        for v in lista:
            no = adicionar(v, no)
        
        print(f'Case {ct+1}:')

        pre_resultado, in_resultado, post_resultado = [], [], []
        prefixa(no, pre_resultado)
        infixa(no, in_resultado)
        posfixa(no, post_resultado)

        print('Pre.:', ' '.join(pre_resultado))
        print('In..:', ' '.join(in_resultado))
        print('Post:', ' '.join(post_resultado))
        print()

if __name__ == "__main__":
    main()