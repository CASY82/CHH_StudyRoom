import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

num.sort()
one = 0
two = len(num) - 1
cnt = 0

if len(num) == 1:
    if num[0] == x:
        print(1)
    else:
        print(0)
else:
    while one < two:
        if num[one] + num[two] > x:
            two -= 1

        elif num[one] + num[two] < x:
            one += 1

        elif num[one] + num[two] == x:
            cnt += 1
            one += 1

    print(cnt)