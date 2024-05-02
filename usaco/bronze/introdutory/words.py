fin = open('word.in', 'r')
fout = open('word.out', 'w')

n, k = fin.readline().split()
p = fin.readline().split()

r = ''
l = []
tl = 0

for pal in p:
    if tl + len(pal) <= int(k):
        l.append(pal)
        tl += len(pal)
    else:
        r += ' '.join(l)+'\n'
        l, tl = [], 0
        l.append(pal)
        tl += len(pal)
        
r += ' '.join(l)
fout.write(r)