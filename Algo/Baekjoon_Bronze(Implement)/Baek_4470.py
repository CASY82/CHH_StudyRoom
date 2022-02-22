import sys

n = int(sys.stdin.readline())

for i in range(n):
    sentense = input()

    print(i+1, ". ", sentense, sep="")