import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentense = input()

    if "Simon says" in sentense:
        sentense = sentense[10:]
        print(sentense)
    else:
        continue