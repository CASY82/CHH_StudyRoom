import sys

n, m = map(int, sys.stdin.readline().split())

a = set()
b = set()

for _ in range(n):
    a.add(sys.stdin.readline().strip())

for _ in range(m):
    b.add(sys.stdin.readline().strip())

c = list(a.intersection(b))
c.sort()

print(len(c))
for i in c:
    print(i)