import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = []
res = set()

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

for merge in permutations(nums, k):
    tmp = "".join(map(str, merge))
    res.add(tmp)

print(len(res))