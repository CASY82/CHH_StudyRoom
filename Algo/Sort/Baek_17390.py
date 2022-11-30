import sys

n, q = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()

nuzuk_hap = [0] + [0 for _ in range(len(num))]
tmp = 0

for i in range(1, len(num)+1):
    nuzuk_hap[i] += num[i-1] + tmp
    tmp += num[i-1]

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())

    print(nuzuk_hap[r] - nuzuk_hap[l-1])