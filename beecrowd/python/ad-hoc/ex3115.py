s1 = [int(i) for i in input().split()]
s2 = [int(i) for i in input().split()]
s3 = [int(i) for i in input().split()]
s4 = [int(i) for i in input().split()]

m = max(sum(s1), sum(s2), sum(s3), sum(s4))
print(f'{m} = {bin(m)[2:]}')