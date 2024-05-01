import sys

n, h = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = 0

for height in array:
    if h >= height:
        result += 1

print(result)