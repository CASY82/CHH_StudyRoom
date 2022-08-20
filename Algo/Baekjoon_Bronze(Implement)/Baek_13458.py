import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

result = n

for i in range(len(a)):
    a[i] -= b

    if a[i] <= 0:
        continue
    else:
        result += a[i] // c
        if a[i] % c != 0:
            result += 1

print(result)