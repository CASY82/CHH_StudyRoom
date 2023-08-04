import sys

mbti = sys.stdin.readline().strip()

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    friend = sys.stdin.readline().strip()

    if friend == mbti:
        result += 1

print(result)