import sys

t = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

for num in test:
    if num == int(num ** 0.5) ** 2:
        print(1, end=" ")
    else:
        print(0, end=" ")