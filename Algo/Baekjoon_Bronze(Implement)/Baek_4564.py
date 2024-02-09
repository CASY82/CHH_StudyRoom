import sys

while True:
    num = sys.stdin.readline().strip()

    if num == "0":
        break

    while len(num) > 1:
        print(num, end=" ")
        tmp = 1

        for i in range(len(num)):
            tmp *= int(num[i])

        num = str(tmp)

    print(num)