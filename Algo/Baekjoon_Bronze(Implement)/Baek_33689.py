import sys

n = int(sys.stdin.readline())
res = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    if word[0] == "C":
        res += 1

print(res)