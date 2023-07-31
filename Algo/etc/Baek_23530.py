import sys

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
all_sum = sum(array)
result = 0

for i in range(len(array)):
    all_sum -= array[i]
    result += (array[i] * all_sum) % 1000000007

print(result % 1000000007)