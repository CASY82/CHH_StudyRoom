import sys

data_set = int(sys.stdin.readline())

for case in range(1, data_set + 1):
    n, w, e = map(int, sys.stdin.readline().split())
    res = 0

    for _ in range(n):
        ww, we, ew, ee = map(int, sys.stdin.readline().split())

        w_ver = w * ww + e * ew
        e_ver = w * we + e * ee

        res += max(w_ver, e_ver)

    print("Data Set {}:".format(case))
    print(res)
    print()