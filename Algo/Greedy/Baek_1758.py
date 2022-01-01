import sys

n = int(sys.stdin.readline())
tips = []
result = 0

for _ in range(n):
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

for i in range(n):
    if tips[i] - i > 0:
        result += tips[i] - i

print(result)