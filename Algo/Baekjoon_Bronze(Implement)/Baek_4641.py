import sys

while True:
    num = list(map(int, sys.stdin.readline().split()))

    if num[0] == -1:
        break

    num.pop()
    tmp = set(num)
    cnt = 0

    for i in range(len(num)):
        if num[i] * 2 in tmp:
            cnt += 1

    print(cnt)