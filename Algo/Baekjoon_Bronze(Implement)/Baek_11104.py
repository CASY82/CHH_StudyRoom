import sys

n = int(sys.stdin.readline())

for _ in range(n):
    binary = list(sys.stdin.readline().strip())
    result = 0
    binary.reverse()
    cnt = 0

    for i in binary:
        if i == "1":
           result += 2 ** cnt

        cnt += 1

    print(result)
