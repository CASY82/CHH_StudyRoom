import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

def max_run_after_deletions(a, k):
    idx = defaultdict(list)
    for i, x in enumerate(a):
        idx[x].append(i)

    ans = 1
    for v, pos in idx.items():
        i = 0

        for j in range(len(pos)):
            while i <= j and (pos[j] - pos[i] - (j - i)) > k:
                i += 1

            ans = max(ans, j - i + 1)

    return ans

print(max_run_after_deletions(nums, k))