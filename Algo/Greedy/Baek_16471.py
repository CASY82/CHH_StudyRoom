import sys

n = int(sys.stdin.readline())

juan = list(map(int, sys.stdin.readline().split()))
sajang = list(map(int, sys.stdin.readline().split()))

juan.sort()
sajang.sort()

cutline = (n + 1) // 2

win_cnt = 0
j = 0

for i in range(n):
    while len(sajang) > j:
        if juan[i] < sajang[j]:
            win_cnt += 1
            j += 1
            break
        else:
            j += 1

if win_cnt >= cutline:
    print("YES")
else:
    print("NO")