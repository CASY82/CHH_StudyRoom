import sys

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

left = 0
removed = 0
maxLen = 0

for right in range(n):
    if s[right] % 2 != 0:
        removed += 1

    while removed > k:
        if s[left] % 2 != 0:
            removed -= 1

        left += 1

    currentEvenCnt = (right - left + 1) - removed
    maxLen = max(maxLen, currentEvenCnt)

print(maxLen)