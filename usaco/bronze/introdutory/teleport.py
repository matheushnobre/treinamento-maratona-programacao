fin = open('teleport.in', 'r')
fout = open('teleport.out', 'w')

a, b, x, y = map(int, fin.readline().split())

o1 = abs(a-x) + abs(b-y)
o2 = abs(a-y) + abs(b-x)
o3 = abs(a-b)

fout.write(str(min(o1, o2, o3)))
fout.close()