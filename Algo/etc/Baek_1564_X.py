import sys

n = int(sys.stdin.readline())

factorial = 1

for i in range(2, n + 1):
    factorial *= i

    while factorial % 10 == 0:
        factorial //= 10

    # 이렇게 나머지를 해줘야 시간 초과가 안난다....
    factorial %= 100000000000000000

print(str(factorial)[-5:])