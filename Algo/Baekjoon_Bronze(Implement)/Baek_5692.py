import sys

fact = [1, 2, 6, 24, 120]

while True:
    num = sys.stdin.readline().strip()
    result = 0

    if num == '0':
        break

    for i in range(len(num)):
        result += int(num[len(num) - 1 - i]) * fact[i]

    print(result)