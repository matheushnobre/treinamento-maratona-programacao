def validar_parenteses(entrada):
    pilha = []
    for caractere in entrada:
        if caractere == '(':
            pilha.append('(')
        elif caractere == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    return True if len(pilha) == 0 else False

while True:
    try:
        entrada = input()
        print("correct") if validar_parenteses(entrada) else print("incorrect")
    except EOFError:
        break