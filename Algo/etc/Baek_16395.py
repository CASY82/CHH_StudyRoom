import sys
import math

n, k = map(int, sys.stdin.readline().split())

tmp_array = []
n = n - 1

for i in range(n + 1):
    tmp_array.append(math.factorial(n) // (math.factorial(i) * math.factorial(n - i)))

print(tmp_array[k - 1])