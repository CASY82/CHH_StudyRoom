import sys

n, k = map(int, sys.stdin.readline().split())

boys = [0 for _ in range(6)]
girls = [0 for _ in range(6)]
room = 0

for _ in range(n):
    s, y = map(int, sys.stdin.readline().split())

    if s == 1:
        boys[y-1] += 1
    else:
        girls[y-1] += 1

for i in range(6):
    room += boys[i] // k + girls[i] // k
    if boys[i] % k != 0:
        room += 1

    if girls[i] % k != 0:
        room += 1

print(room)