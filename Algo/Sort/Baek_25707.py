import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
result = 0

array.sort()

for i in range(1, len(array)):
    result += abs(array[i-1] - array[i])

result += abs(array[i] - array[0])

print(result)