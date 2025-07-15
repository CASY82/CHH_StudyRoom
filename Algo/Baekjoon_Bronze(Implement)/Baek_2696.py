import sys

n, m = map(int, sys.stdin.readline().split())
skill = []

for _ in range(n):
    dot, time = map(int, sys.stdin.readline().split())

    skill.append([dot, time])

skill.sort(key=lambda x: (-x[0], -x[1]))

max_damage = 0
max_time = 999999999999999

for i in range(m):
    max_damage += skill[i][0]
    max_time = min(max_time, skill[i][1])

print(max_damage, max_time)