# Dongjak N1
import sys

n = int(sys.stdin.readline())
station = list(map(int, sys.stdin.readline().split()))

station.sort()
distance = dict()
min_dis = 999999999999999999999

for i in range(n - 1):
    tmp = station[i + 1] - station[i]

    if tmp not in distance:
        distance[tmp] = 1
    else:
        distance[tmp] += 1

    min_dis = min(tmp, min_dis)

print(min_dis, distance[min_dis])