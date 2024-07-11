import sys

n = int(sys.stdin.readline())
check = True

money, boss_atk = map(int, sys.stdin.readline().split())

for _ in range(n):
    cost, damage = map(int, sys.stdin.readline().split())

    if cost <= money and damage > boss_atk:
        check = False
        break

if check:
    print("NO")
else:
    print("YES")