import sys

s = sys.stdin.readline().strip()
pre = []

for i in range(len(s)):
    pre.append(s[i:])

pre.sort()

for j in pre:
    print(j)