n = int(input())
l = set()
for _ in range(2):
    for v in input().split()[1:]:
        l.add(int(v))
print('I become the guy.') if len(l) == n else print('Oh, my keyboard!')