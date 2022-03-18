import sys

a, b, c = map(int, sys.stdin.readline().split())
truck = []
result = 0

for _ in range(3):
    truck.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, 101):
    now = 0

    if truck[0][0] <= i < truck[0][1]:
        now += 1

    if truck[1][0] <= i < truck[1][1]:
        now += 1

    if truck[2][0] <= i < truck[2][1]:
        now += 1

    if now == 1:
        result += a
    elif now == 2:
        result += b * 2
    elif now == 3:
        result += c * 3

print(result)