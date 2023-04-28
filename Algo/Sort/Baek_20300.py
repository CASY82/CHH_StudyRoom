import sys

n = int(sys.stdin.readline())
muscle = list(map(int, sys.stdin.readline().split()))

muscle.sort()
maxi = 0

if len(muscle) % 2 == 1:
    tmp = muscle[:len(muscle)-1]

    for i in range(len(tmp)//2):
        if maxi < (tmp[i] + tmp[len(tmp) - 1 - i]):
            maxi = tmp[i] + tmp[len(tmp) - 1 - i]

    if maxi < muscle[-1]:
        print(muscle[-1])
    else:
        print(maxi)
else:
    for i in range(len(muscle)//2):
        if maxi < (muscle[i] + muscle[len(muscle) - 1 - i]):
            maxi = muscle[i] + muscle[len(muscle) - 1 - i]

    print(maxi)