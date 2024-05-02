fin = open('speeding.in', 'r')
fout = open('speeding.out', 'w')

n, m = map(int, fin.readline().split())

vp = []
for i in range(n):
    a, b = map(int, fin.readline().split())
    v = [b] * a
    vp.extend(v)
    
vr = []
for i in range(m):
    a, b = map(int, fin.readline().split())
    v = [b] * a
    vr.extend(v)
    
me = 0
for i in range(100):
    e = vr[i] - vp[i]
    if e > me:
        me = e

fout.write(str(me))
fout.close()