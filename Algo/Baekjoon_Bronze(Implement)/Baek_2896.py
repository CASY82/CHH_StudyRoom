import sys

while True:
    sentense = list(sys.stdin.readline().strip().split())

    if sentense[0] == "#":
        break

    for word in sentense:
        print(word[::-1], end=" ")

    print()