import sys

t = int(sys.stdin.readline())

for _ in range(t):
    suOne = int(sys.stdin.readline())
    suOneNumList = set(map(int, sys.stdin.readline().split()))

    suTwo = int(sys.stdin.readline())
    suTwoNumList = map(int, sys.stdin.readline().split())

    for i in suTwoNumList:
        if i in suOneNumList:
            print(1)
        else:
            print(0)