import sys

e, f, c = map(int, sys.stdin.readline().split())

total = e + f
result = 0
remain = 0

while True:
    remain = total % c
    total //= c

    if total <= 0:
        break

    result += total

    total += remain

print(result)
