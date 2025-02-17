import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    ans = []

    length = tmp[0]
    tmp = tmp[1:]
    tmp = tmp[::-1]

    for i in range(length + 1):
        if i == 0:
            continue
        else:
            ans.append(i * tmp[i])

    ans.append(length - 1)
    ans = ans[::-1]

    print("Case {0}:".format(case), *ans)