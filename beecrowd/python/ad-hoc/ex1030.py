num_testes = int(input())
teste = 1
while teste <= num_testes:
    # Lendo a quantidade de pessoas no círculo e o tamanho do salto
    pessoas, salto = map(int, input().split())
    
    # Criando lista com os jogadores
    jogadores = [i+1 for i in range(pessoas)]
    
    # Inicializando variável que irá armazenar qual jogador deve ser eliminado
    posicao = (salto - 1) % len(jogadores)
    
    # Laço de repetição que irá ser executado enquanto não for determinado o vencedor
    while len(jogadores) > 1:
        jogadores.pop(posicao)
        posicao = (posicao + salto - 1) % len(jogadores)
        
    print('Case {}: {}'.format(teste, jogadores[0]))
    teste += 1