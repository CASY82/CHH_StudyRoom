import sys

a1, a2, a3, b1, b2, b3, l = map(int, sys.stdin.readline().split())

tmp = [(a1, b1), (a2, b2), (a3, b3)]

tmp.sort(key=lambda x:-x[0])
cnt = 0
res = 0
check = False

for cost, val in tmp:
    for i in range(1, val + 1):
        if res < l:
            res += cost
            cnt += 1
        else:
            check = True
            break

    if check:
        break

if res < l:
    print(0)
else:
    print(cnt)