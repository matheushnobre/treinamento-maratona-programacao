e = input()
m = 0

ls = e[0]
ns = 0
for l in e:
    if l == ls:
        ns += 1
    else:
        if ns > m:
            m = ns
        ls = l
        ns = 1
        
print(max(m, ns))