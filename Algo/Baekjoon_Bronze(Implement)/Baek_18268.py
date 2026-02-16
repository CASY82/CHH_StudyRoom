# Cow Gymnastics
import sys

n, k = map(int, sys.stdin.readline().split())

pos = [[0] * (k + 1) for _ in range(n)]

for case in range(n):
    cows = list(map(int, sys.stdin.readline().split()))

    for i in range(k):
        cow = cows[i]
        pos[case][cow] = i

ans = 0

for a in range(1, k + 1):
    for b in range(1, k + 1):
        if a == b:
            continue

        consistent = True

        for case in range(n):
            if pos[case][a] > pos[case][b]:
                consistent = False
                break

        if consistent:
            ans += 1

print(ans)