import sys

data = list(map(int, sys.stdin.readline().split()))

pos = [0]

for i in data:
    pos.append(pos[-1] + i)

for i in range(5):
    row = [str(abs(pos[j] - pos[i])) for j in range(5)]
    print(*row)