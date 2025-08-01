import sys

n = int(sys.stdin.readline())
level = []

for _ in range(n):
    level.append(int(sys.stdin.readline()))

if level[0] == min(level):
    print("ez")
elif level[0] == max(level):
    print("hard")
else:
    print("?")