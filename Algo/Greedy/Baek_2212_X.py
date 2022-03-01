import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
distance = []

sensor.sort()

for i in range(1, len(sensor)):
    distance.append(abs(sensor[i] - sensor[i - 1]))

distance.sort()

for i in range(k-1):
    # n < k인 경우는 생각을 못했음
    if distance:
        distance.pop()
    else:
        break

print(sum(distance))