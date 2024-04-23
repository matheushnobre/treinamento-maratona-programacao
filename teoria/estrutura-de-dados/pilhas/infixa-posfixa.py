from pilha import Stack

def infixaParaPosfixa(expressao):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    operandos = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    # Passo 1: Crie uma pilha vazia chamada opstack para manter os operadores. Crie uma lista vazia para a saída
    opstack = Stack()
    lsaida = []
    
    # Passo 2: Converta string infixa para uma lista
    expressao = list(expressao)
    
    # Passo 3: Examine os itens da lista da esquerda para a direita
    # 3.1 Se o item é um operando, coloque-o no final da lista da saída.
    # 3.2 Se o item é um abre parêntese, insira.o no final da lista da saída
    # 3.3 Se o item é um fecha parênteses, remova ( pop()) os itens de opstack até que o abre parêntese correspondente seja removido. 
    # Coloque cada operador removido no final da lista da saída.
    # 3.4 Se i item é um operador, *, /, +, or -, insira-o na pilha opstack. Entretanto, remova antes os operadores que estão na pilha que têm 
    # precedência maior ou igual ao operador encontrado e coloque-os na final da lista da saída.
    for item in expressao:
        if item in operandos:
            lsaida.append(item)
        elif item == '(':
            opstack.push(item)
        elif item == ')':
            topStack = opstack.pop()
            while topStack != '(':
                lsaida.append(topStack)
                topStack = opstack.pop()
        elif item in prec:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[item]):
                lsaida.append(opstack.pop())
            opstack.push(item)
            
    # Passo 4: Quando a expressão tiver sido completamente examinada, verifique opstack. Qualquer operador que ainda está na pilha deve ser 
    # removido e colocado na lista da saída.
    while not opstack.isEmpty():
        lsaida.append(opstack.pop())
        
    return " ".join(lsaida)

print(infixaParaPosfixa("( A + B ) * ( C + D )"))
print(infixaParaPosfixa("( A + B ) * C"))
print(infixaParaPosfixa("A + B * C"))