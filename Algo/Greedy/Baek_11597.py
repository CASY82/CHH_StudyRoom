import sys

n = int(sys.stdin.readline())
team = []

for _ in range(n):
    team.append(int(sys.stdin.readline()))

team.sort()

result = int(1e9)

for i in range(n // 2):
    result = min(team[i] + team[len(team) - 1 - i], result)

print(result)