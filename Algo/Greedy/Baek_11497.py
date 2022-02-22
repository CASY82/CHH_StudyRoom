import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    logs = list(map(int, sys.stdin.readline().split()))
    tmp = [0 for i in range(n)]

    logs.sort()
    k = 0
    for i in range(len(logs)):
        if i % 2 == 0:
            tmp[k] = logs[i]
            k += 1
        else:
            tmp[-k] = logs[i]

    max_diff = 0
    for i in range(len(tmp)-1):
        if max_diff < abs(tmp[i] - tmp[i + 1]):
            max_diff = abs(tmp[i] - tmp[i + 1])

    print(max_diff)

#더 쉬운 풀이가...
# for _ in range(int(input())):
#     n=int(input())
#     l=sorted(list(map(int, input().split())))
#     r=0
#     for i in range(len(l)-2):
#         r=max(l[i+2]-l[i], r)
#     print(r)