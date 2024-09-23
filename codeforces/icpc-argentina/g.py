string = input()
menorTP = min(string.count('T'), string.count('P'))
totalAU = string.count('A') + string.count('U')
print(min(menorTP, totalAU))