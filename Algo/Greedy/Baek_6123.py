import sys

n, l, k = map(int, sys.stdin.readline().split())

cow_charm = []
cnt = 0

for _ in range(n):
    cow_charm.append(int(sys.stdin.readline()))

cow_charm.sort()

for i in range(n):
    if cow_charm[i] <= l:
        l += k
        cnt += 1
    else:
        break

print(cnt)