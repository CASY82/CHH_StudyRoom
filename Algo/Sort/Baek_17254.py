import sys

n, m = map(int, sys.stdin.readline().split())
keyboard = []

for _ in range(m):
    a, b, c = sys.stdin.readline().strip().split()

    keyboard.append([int(a), int(b), c])

keyboard.sort(key=lambda x:(x[1], x[0]))
res = ""

for i in range(m):
    res += keyboard[i][2]

print(res)