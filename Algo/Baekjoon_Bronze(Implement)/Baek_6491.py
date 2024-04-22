import sys
import math

nums = list(map(int, sys.stdin.read().split()))

for num in nums:
    if num == 0:
        break

    tmp = []

    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i == 0:
            if num // i != i:
                tmp.append(num // i)
                tmp.append(i)
            else:
                tmp.append(i)

    sum_nums = sum(tmp[1:])

    if sum_nums < tmp[0]:
        print(tmp[0], "DEFICIENT")
    elif sum_nums == tmp[0]:
        print(tmp[0], "PERFECT")
    else:
        print(tmp[0], "ABUNDANT")