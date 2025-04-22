import sys

n = int(sys.stdin.readline())
res = 0
passport = set()

for _ in range(n):
    passport.add(sys.stdin.readline().strip())

m = int(sys.stdin.readline())

for _ in range(m):
    tmp = sys.stdin.readline().strip()

    if tmp in passport:
        res += 1

print(res)