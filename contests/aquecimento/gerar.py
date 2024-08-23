import random

saida = open('entrada.txt', 'w')
saida.write('239 241\n')

for i in range(239):
    for j in range(241):
        num = random.randint(1, 100)
        saida.write(str(num)+' ')
    saida.write('\n')