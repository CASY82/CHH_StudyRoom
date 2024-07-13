import sys

n, s = map(int, sys.stdin.readline().split())

cow = []
res = 0

for _ in range(n):
    cow.append(int(sys.stdin.readline()))

cow.sort()

left, right = 0, n - 1
while left < right:
    if cow[left] + cow[right] <= s:
        res += right - left
        left += 1
    else:
        right -= 1

print(res)