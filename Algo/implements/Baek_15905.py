import sys

n = int(sys.stdin.readline())

participate = []
result = 0

for _ in range(n):
    solve, penalty = map(int, sys.stdin.readline().split())
    participate.append((solve, penalty))

participate.sort(key=lambda x : (-x[0], x[1]))

if n > 5:
    for i in range(5, len(participate)):
        if participate[4][0] == participate[i][0]:
            result += 1

    print(result)
else:
    print(0)