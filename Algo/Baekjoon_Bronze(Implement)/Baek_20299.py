import sys

n, k, l = map(int, sys.stdin.readline().split())
result = []
team = 0

for _ in range(n):
    one, two, three = map(int, sys.stdin.readline().split())
    able = True

    for rate in (one, two, three):
        if rate < l:
            able = False
            break

    if one + two + three < k:
        able = False

    if able:
        for rate in (one, two, three):
            result.append(rate)
        team += 1

print(team)
print(*result)