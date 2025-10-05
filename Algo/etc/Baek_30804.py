import sys
from collections import defaultdict

n = int(sys.stdin.readline())
tanghuru = list(map(int, sys.stdin.readline().split()))

cnt = defaultdict(int)
left = 0
distinct = 0
ans = 0

for right in range(n):
    x = tanghuru[right]
    if cnt[x] == 0:
        distinct += 1
    cnt[x] += 1

    while distinct > 2:
        y = tanghuru[left]
        cnt[y] -= 1

        if cnt[y] == 0:
            distinct -= 1
            del cnt[y]

        left += 1

    ans = max(ans, right - left + 1)

print(ans)