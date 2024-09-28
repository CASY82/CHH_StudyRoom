import sys

n = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))

value.sort()

if n % 2 == 0:
    print(sum(value[n // 2:]))
else:
    print(sum(value[n // 2 + 1:]))