# Baby Bites

import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip().split())
now = 0
check = True

for i in word:
    if i.isdigit():
        tmp = int(i)
        if tmp - 1 == now:
            now = int(i)
        else:
            check = False
            break
    else:
        now += 1

if check:
    print("makes sense")
else:
    print("something is fishy")