import sys

while True:
    num = sys.stdin.readline().strip()

    if num == '0':
        break

    tmp = num

    while True:
        result = 0

        for i in tmp:
            result += int(i)

        if result < 10:
            break
        else:
            tmp = str(result)

    print(result)