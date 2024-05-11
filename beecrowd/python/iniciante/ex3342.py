n = int(input())
tc = n*n

if tc % 2 == 0:
    b = p = tc/2
else:
    b = tc//2 + 1
    p = tc//2
    
print(f'{b:.0f} casas brancas e {p:.0f} casas pretas')
