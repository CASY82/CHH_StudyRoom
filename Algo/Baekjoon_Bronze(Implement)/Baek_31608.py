import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
res = 0

for i in range(n):
    if s[i] != t[i]:
       res += 1

print(res)