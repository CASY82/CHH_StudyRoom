import sys

while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break

    result = 0

    for i in range(num+1):
        result += i

    print(result)