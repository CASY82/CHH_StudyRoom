# k-сортировка
import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
res = True

if k > 1:
    origin = [0] * n
    switch = [0] * n

    for i in range(n):
        origin[i] = nums[i] % k

    nums.sort()

    for j in range(n):
        switch[j] = nums[j] % k

    for i in range(n):
        if origin[i] != switch[i]:
            res = False
            break

if res:
    print("YES")
else:
    print("NO")