import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
good = 0
bad = 0

for i in range(n):
    if num_list[i] % 2 == 0:
        good += 1
    else:
        bad += 1

if good > bad:
    print("Happy")
else:
    print("Sad")