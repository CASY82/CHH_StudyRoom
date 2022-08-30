import sys

n = int(sys.stdin.readline())

for _ in range(n):
    nick = list(sys.stdin.readline().strip().split())

    nick[0] = 'god'

    for i in range(len(nick)):
        print(nick[i], end='')

    print()