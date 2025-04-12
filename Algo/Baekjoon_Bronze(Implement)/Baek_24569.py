import sys

n = int(sys.stdin.readline())
res = [0 for _ in range(n)]

# 득점
for i in range(n):
    res[i] += 5 * int(sys.stdin.readline())
    res[i] -= 3 * int(sys.stdin.readline())

final = 0

for k in range(n):
    if res[k] > 40:
        final += 1

if final == n:
    print(str(final) + "+")
else:
    print(final)