fin = open('mixmilk.in', 'r')
fout = open('mixmilk.out', 'w')

cap, milk = [0]*3, [0]*3
for i in range(3):
    cap[i], milk[i]= map(int, fin.readline().split())

for i in range(100):
    b1 = i % 3
    b2 = (i + 1) % 3

    amt = min(milk[b1], cap[b2] - milk[b2])
    milk[b1] -= amt
    milk[b2] += amt
    
s = '\n'.join(map(str, milk))
fout.write(s)
fout.close()