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