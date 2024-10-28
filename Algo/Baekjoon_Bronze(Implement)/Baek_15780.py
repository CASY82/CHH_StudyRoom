import sys

n, k = map(int, sys.stdin.readline().split())
multitap = list(map(int, sys.stdin.readline().split()))

can_use_code = 0

for i in range(k):
    if multitap[i] % 2 == 1:
        can_use_code += multitap[i] // 2 + 1
    else:
        can_use_code += multitap[i] // 2

if can_use_code < n:
    print("NO")
else:
    print("YES")