# 순열 사이클
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    res = 0

    nodes = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        nodes[i].append(nums[i - 1])

    visited[0] = 1

    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            tmp = nodes[i][0]
            while True:
                visited[tmp] = 1
                tmp = nodes[tmp][0]
                if tmp == i:
                    break

            res += 1

    print(res)