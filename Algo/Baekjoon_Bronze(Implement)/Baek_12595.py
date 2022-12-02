import sys

n = int(sys.stdin.readline())

for cnt in range(n):
    g = int(sys.stdin.readline())
    sonnom = list(map(int, sys.stdin.readline().split()))
    tmp = dict()
    result = []

    for i in range(len(sonnom)):
        if sonnom[i] not in tmp:
            tmp[sonnom[i]] = 1
        else:
            tmp[sonnom[i]] += 1

    for key, value in tmp.items():
        if value == 1:
            result.append(key)

    print("Case #{}:".format(cnt + 1), *result)