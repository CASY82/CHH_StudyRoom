import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    skills = sys.stdin.readline().strip()

    if skills.find("CD") != -1:
        continue

    result += 1

print(result)