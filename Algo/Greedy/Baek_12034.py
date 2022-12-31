import sys

t = int(sys.stdin.readline())

for cnt in range(t):
    n = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    result = []

    i = 0
    while num:
        discount = int(num[i] * 0.75)
        if discount in num:
            num.remove(discount)
            i -= 1
            num.remove(num[i])
            result.append(discount)
        else:
            i += 1
            continue

    print("Case #{}:".format(cnt + 1), *result)