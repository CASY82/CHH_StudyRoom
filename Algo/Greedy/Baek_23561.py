import sys

n = int(sys.stdin.readline())
participant = list(map(int, sys.stdin.readline().split()))

participant.sort()

print(participant[2 * n - 1] - participant[n])