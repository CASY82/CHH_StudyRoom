import sys

n = int(sys.stdin.readline())

def rounds(num, cnt):
    loc = 10 ** cnt
    tmp = num % loc

    if tmp >= 5 * (loc//10):
        num += loc-tmp
    else:
        num -= tmp

    return num

for _ in range(n):
    num = int(sys.stdin.readline())
    result = num
    cnt = 1

    if num >= 10:
        while result >= 10 ** cnt:
            result = rounds(result, cnt)
            cnt += 1
    else:
        result = num

    print(result)