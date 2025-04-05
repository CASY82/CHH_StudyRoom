import math
import sys

i = int(sys.stdin.readline())
num_set = set()

for num in range(1, int(math.sqrt(i)) + 1):
    if i % num == 0:
        num_set.add(num)
        num_set.add(i // num)

print(sum(num_set))