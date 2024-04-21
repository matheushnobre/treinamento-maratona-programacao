nm = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
valor = float(input())

for nota_moeda in nm: 
    qtd_necessaria = int(valor / nota_moeda) 
    valor = round(valor % nota_moeda, 2)
    
    nm[nota_moeda] = qtd_necessaria
    
print("NOTAS:")
for index, nota_moeda in enumerate(nm):
    if index < 6:
        print("{} nota(s) de R$ {:.2f}".format(nm[nota_moeda], nota_moeda))
    elif index == 6:
        print("MOEDAS:")
        print("{} moeda(s) de R$ {:.2f}".format(nm[nota_moeda], nota_moeda))
    else:
        print("{} moeda(s) de R$ {:.2f}".format(nm[nota_moeda], nota_moeda))