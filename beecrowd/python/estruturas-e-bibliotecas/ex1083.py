operadores = {'^': 6, '*': 5, '/': 5, '+': 4, '-': 4, '>': 3, '<': 3, '=': 3, '#': 3, '.': 2, '|': 1}
operandos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

def isValid(expressao):
    stack = []
    isOperador = False
    if expressao[0] in operadores or expressao[-1] in operadores:
        return 'Syntax Error!'
    for index, e in enumerate(expressao): 
        if e in operadores:
            if isOperador:
                return 'Syntax Error!'
            else:
                isOperador = True
        else:
            isOperador = False
        if e == '(':
            stack.append('(')
        elif e == ')':
            if len(stack) == 0:
                return 'Syntax Error!'
            stack.pop()
        elif e not in operadores and e not in operandos:
            return 'Lexical Error!'

    if len(stack) == 0:
        return converterPosfixa(expressao)
    else:
        return 'Syntax Error!'
    
def converterPosfixa(expressao):
    oppilha = []
    listsaida = []
    expressao = list(expressao)
    for e in expressao:
        if e in operandos:
            listsaida.append(e)
        elif e == '(':
            oppilha.append('(')
        elif e == ')':
            item = oppilha.pop()
            while item != '(':
                listsaida.append(item)
                item = oppilha.pop()
        else:
            while (not len(oppilha) == 0) and (oppilha[-1] != '('):
                if operadores[oppilha[-1]] >= operadores[e]:
                    listsaida.append(oppilha.pop())
                else:
                    break
            oppilha.append(e)
    while len(oppilha) != 0:
        listsaida.append(oppilha.pop())
    return "".join(listsaida)       
    
while True:
    try:
        expressao = input()
        print(isValid(expressao))
    except EOFError: 
        break