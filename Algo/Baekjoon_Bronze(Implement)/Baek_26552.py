import sys

n = int(sys.stdin.readline())

for _ in range(n):
    num = sys.stdin.readline().strip()

    while True:
        tmp = int(num)
        tmp += 1
        num = str(tmp)

        if num.count("0") == 0:
            print(num)
            break