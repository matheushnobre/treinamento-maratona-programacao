entrada = input().split(' ')
h1, m1, h2, m2 = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])

m1 += h1 * 60
m2 += h2 * 60
tempo = m2 - m1

if tempo <= 0:
    tempo += 24 * 60
    
h3 = tempo // 60
m3 = tempo % 60
    
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h3, m3))