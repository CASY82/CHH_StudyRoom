import sys

n = int(sys.stdin.readline())
check = [n]

def calc(num):
    tmp = list(str(num))
    res = 0

    for i in range(len(tmp)):
        res += int(tmp[i]) * int(tmp[i])

    return res

while True:
    n = calc(n)

    if n in check:
        check.append(n)
        break
    else:
        check.append(n)

if 1 in check:
    print("HAPPY")
else:
    print("UNHAPPY")