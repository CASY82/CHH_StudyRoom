import sys

n = int(sys.stdin.readline())

for _ in range(n):
    card_num = list(sys.stdin.readline().strip())

    result = 0

    for i in range(16):
        if i % 2 == 0:
            tmp = int(card_num[i]) * 2

            if tmp >= 10:
                result += 1 + (tmp % 10)
            else:
                result += tmp
        else:
            result += int(card_num[i])

    if result % 10 == 0:
        print("T")
    else:
        print("F")