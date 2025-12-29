import sys

res = 0

for _ in range(4):
    type, height = sys.stdin.readline().strip().split()

    height = int(height)

    if type == "Es":
        res += height * 21
    else:
        res += height * 17

print(res)