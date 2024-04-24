import sys

n = int(sys.stdin.readline())

# 0 : odd / 1: even
check = set()

for i in range(1, 101):
    total = 0
    for j in range(i, i + n):
        total += j

    if total % 2 == 0:
        check.add(1)
    else:
        check.add(0)

if len(check) == 2:
    print("Either")
elif len(check) == 1:
    if 1 in check:
        print("Even")
    else:
        print("Odd")