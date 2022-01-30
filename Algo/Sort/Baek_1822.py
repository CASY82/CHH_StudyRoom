import sys

n, m = map(int, sys.stdin.readline().split())

numA = list(map(int, sys.stdin.readline().split()))
a = set(numA)

numB = list(map(int, sys.stdin.readline().split()))
b = set(numB)

result =list(a-b)
result.sort()

print(len(result))
for i in result:
    print(i, end=' ')