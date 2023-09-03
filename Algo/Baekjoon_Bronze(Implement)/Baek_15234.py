import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        if k == numbers[i] + numbers[j]:
            result += 1

print(result)