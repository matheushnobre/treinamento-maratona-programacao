from fractions import Fraction

# função para ler a expressão e retornar os numeradores e denomidadores das frações, além do operador
def sistematizar(expressao):
    expressao = expressao.split(' ')
    n1, d1, operador, n2, d2 = int(expressao[0]), int(expressao[2]), expressao[3], int(expressao[4]), int(expressao[6])
    return n1, d1, operador, n2, d2

def somar(n1, d1, n2, d2):
    return (n1*d2 + n2*d1), (d1*d2)

def subtrair(n1, d1, n2, d2):
    return (n1*d2 - n2*d1), (d1*d2)

def multiplicar(n1, d1, n2, d2):
    return (n1*n2), (d1*d2)

def dividir(n1, d1, n2, d2):
    return (n1*d2), (n2*d1)

testes = int(input())

for i in range(testes):
    expressao = input()
    n1, d1, operador, n2, d2 = sistematizar(expressao)
    
    match(operador):
        case '+':
            n3, d3 = somar(n1, d1, n2, d2)
            fracao = Fraction(n3, d3) # O Fraction irá simplificar a fração
        case '-':
            n3, d3 = subtrair(n1, d1, n2, d2)
            fracao = Fraction(n3, d3)
        case '*':
            n3, d3 = multiplicar(n1, d1, n2, d2)
            fracao = Fraction(n3, d3)
        case '/':
            n3, d3 = dividir(n1, d1, n2, d2)
            fracao = Fraction(n3, d3)
            
    print("{}/{} = {}/{}".format(n3, d3, fracao.numerator, fracao.denominator))
    