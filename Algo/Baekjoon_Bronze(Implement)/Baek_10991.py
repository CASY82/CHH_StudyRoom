import sys

n = int(sys.stdin.readline())

for i in range(n):
    tmp = n-1
    star = 0
    cnt = 0
    for j in range(2 * n - 1):
        if j == tmp + i - cnt:
            print("*", end='')
            star += 1
            if cnt < i:
                cnt -= 2
        elif j == tmp - i + cnt:
            print("*", end='')
            star += 1
            if cnt < i:
                cnt += 2
        else:
            print(" ", end='')

        if j == tmp:
            cnt -= 2

        if star == i+1:
            break

    print()
