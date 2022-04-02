import sys

n = int(sys.stdin.readline())

peaks = list(map(int, sys.stdin.readline().split()))
tmp = 0
compare = 0
max_kill = 0

for i in peaks:
    if compare < i:
        compare = i
        tmp = 0

    else:
        tmp += 1

    if max_kill < tmp:
        max_kill = tmp

print(max_kill)