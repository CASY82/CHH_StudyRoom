#올바른 배열
import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort()

ans = 5
j = 0

for i in range(n):

    while j < n and arr[j] <= arr[i] + 4:
        j += 1

    count_in_range = j - i
    ans = min(ans, 5 - count_in_range)

print(ans)