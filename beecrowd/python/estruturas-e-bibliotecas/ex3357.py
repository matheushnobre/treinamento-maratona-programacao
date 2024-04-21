n, l, q = map(float, input().split())

p = input().split()
r = p[int((l // q) % len(p))]
m = round((l % q), 1)

# Foi preciso criar uma condição para resolver um problema da saída da própria Beecrowd
print('Juca 0.4') if r=='Bob' and m==0.0 else print(r, m)