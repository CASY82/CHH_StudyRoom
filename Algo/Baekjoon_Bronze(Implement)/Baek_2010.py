import sys

n = int(sys.stdin.readline())
multitap = []
computer = 0

for i in range(n):
    multitap.append(int(sys.stdin.readline()))

for i in range(len(multitap)):
    if i != len(multitap) - 1:
        multitap[i] -= 1

    computer += multitap[i]

print(computer)