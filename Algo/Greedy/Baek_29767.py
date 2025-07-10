import sys

n, k = map(int, sys.stdin.readline().split())
rooms = list(map(int, sys.stdin.readline().split()))

rooms_sum = [rooms[0]]

for i in range(1, n):
    rooms_sum.append(rooms_sum[i - 1] + rooms[i])

rooms_sum.sort(reverse=True)

res = 0

for j in range(k):
    res += rooms_sum[j]

print(res)