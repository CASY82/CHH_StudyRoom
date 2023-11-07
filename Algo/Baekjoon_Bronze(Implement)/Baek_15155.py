import sys

n, k = map(int, sys.stdin.readline().split())
writing = list(map(int, sys.stdin.readline().split()))

notes = 1
tmp = k

for i in range(n):
    tmp -= writing[i]

    if tmp < 0:
        tmp = k - writing[i]
        notes += 1

print(notes)