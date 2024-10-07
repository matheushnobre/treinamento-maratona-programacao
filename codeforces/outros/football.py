n = int(input())
teams = []
goals = [0, 0]

for i in range(n):
    t = input()
    if t not in teams:
        teams.append(t)
    goals[teams.index(t)] += 1
    
if goals[0] > goals[1]:
    print(teams[0])
else:
    print(teams[1])