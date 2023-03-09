import sys

n = int(sys.stdin.readline())

hubo = []

for _ in range(n):
    name, score = sys.stdin.readline().strip().split()
    score = int(score)

    hubo.append([name, score])

hubo.sort(key=lambda x:(-x[1], x[0]))

print(hubo[0][0])