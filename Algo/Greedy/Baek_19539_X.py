import sys

n = int(sys.stdin.readline())
apple_tree = list(map(int, sys.stdin.readline().strip().split()))

check = True
sum_tree = sum(apple_tree)
tmp = sum_tree // 3

if sum_tree % 3 != 0:
    check = False
else:
    for i in apple_tree:
        if i // 2 > 0:
            tmp -= (i // 2)

    if tmp > 0:
        check = False

if check:
    print("YES")
else:
    print("NO")