import sys

n, k = map(int, sys.stdin.readline().split())
quest = list(map(int, sys.stdin.readline().split()))

quest.sort()
active_stone = 0
result = 0

for exp in range(len(quest)):
    if active_stone == 0:
        active_stone += 1
    else:
        result += quest[exp] * active_stone
        if active_stone < k:
            active_stone += 1

print(result)