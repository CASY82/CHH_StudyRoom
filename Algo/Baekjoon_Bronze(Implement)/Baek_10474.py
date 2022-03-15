import sys

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == b == 0:
        break

    mock = a // b
    a -= mock * b

    print(mock, a, "/", b)