import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

for i in range(n - 1):
    if s[i + 1] == "J":
        print(s[i])