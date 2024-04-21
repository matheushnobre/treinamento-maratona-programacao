def gerador_pilotos(num_pilotos):
    pilotos = {}
    for i in range(num_pilotos):
        pilotos.update({str(1+i): 0}) # Adiciona o piloto ao dicionário. Sua pontuação inicia em 0
    return pilotos

def gerar_campeao(pilotos):
    maior = 0
    campeoes = ''
    for piloto in pilotos:
        if pilotos[piloto] == maior:
            campeoes += ' '+ piloto
        elif pilotos[piloto] > maior:
            campeoes = piloto
            maior = pilotos[piloto]
    return campeoes

while True:
    # Lendo o número de grande prêmios e o número de pilotos
    num_gp, num_pilotos = map(int, input().split(' '))
    
    if num_gp == 0 & num_pilotos == 0:
        break

    # Lendo o resultado de cada grande prêmio
    resultados = []
    for gp in range(num_gp):
        resultados.append(input().split(' '))

    # Lendo o número de sistemas de pontuação
    num_sistemas = int(input())

    # Percorrendo cada sistema
    for sistema in range(num_sistemas):
        pilotos = gerador_pilotos(num_pilotos) # Reseta a pontuação dos pilotos
        sistema_pontuacao = input().split(' ')
        ultimo_pontuador = sistema_pontuacao.pop(0)
        
        # Percorrendo o resultado de cada corrida
        for resultado in resultados:
            for index, classificacao in enumerate(resultado):
                piloto = str(index+1)
                if int(classificacao) <= int(ultimo_pontuador):
                    pilotos[piloto] = pilotos[piloto] + int(sistema_pontuacao[int(classificacao)-1])
        
        print(gerar_campeao(pilotos))