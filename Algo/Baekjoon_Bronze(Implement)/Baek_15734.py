import sys

l, r, a = map(int, sys.stdin.readline().split())

min_num = min(l, r) + a
max_num = max(l, r)

if min_num > max_num:
    tmp_diff = abs(l-r)

    tmp = (a - tmp_diff) // 2

    print((max_num + tmp) * 2)
else:
    print(min_num * 2)