import sys

n, k = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))

left = 0
cnt_one = 0
res = float('inf')

for right in range(n):
    if dolls[right] == 1:
        cnt_one += 1

    while cnt_one >= k:
        if cnt_one == k:
            res = min(res, right - left + 1)

        if dolls[left] == 1:
            cnt_one -= 1
        left += 1

if res != float('inf'):
    print(res)
else:
    print(-1)