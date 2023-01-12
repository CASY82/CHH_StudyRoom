import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

result = n

for _ in range(k):
    n *= 10
    result += n

print(result)