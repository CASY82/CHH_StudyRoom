import sys

n, k = map(int, sys.stdin.readline().split())
teams = []
university = set()

for _ in range(n):
    uni_name, team_name, solve, penalty = sys.stdin.readline().strip().split()

    solve = int(solve)
    penalty = int(penalty)

    teams.append([uni_name, team_name, solve, penalty])

teams.sort(key=lambda x:(-x[2], x[3]))

for i in range(n):
    if len(university) == k:
        break

    if teams[i][0] not in university:
        university.add(teams[i][0])
        print(teams[i][1])