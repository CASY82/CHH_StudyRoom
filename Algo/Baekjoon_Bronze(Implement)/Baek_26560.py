import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentense = sys.stdin.readline().strip()

    if sentense[-1] != '.':
        sentense += '.'

    print(sentense)