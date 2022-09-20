import sys

while True:
    ori_days = int(sys.stdin.readline())
    days = ori_days
    result = 0

    if days == 0:
        break

    tmp = 1
    while days >= 0:
        days -= tmp
        result += tmp * tmp
        tmp += 1

    if days < 0:
        tmp -= 1
        days += tmp
        result -= tmp * tmp
        result += tmp * days

    print(ori_days, result)