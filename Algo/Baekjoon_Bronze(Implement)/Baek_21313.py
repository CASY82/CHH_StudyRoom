import sys

n = int(sys.stdin.readline())
res = ""

if n % 2 == 1:
    if n == 1:
        res = "1"
    else:
        for _ in range(n // 2):
            res = res + "1 2 "

        res = res + "3"
else:
    for _ in range(n // 2):
        res = res + "1 2 "

    res.rstrip()

print(res)