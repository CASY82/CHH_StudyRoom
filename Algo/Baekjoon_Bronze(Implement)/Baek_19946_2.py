import sys
import math

n = int(sys.stdin.readline().strip())

while n % 2 == 0:
    n //= 2

n += 1
print(int(math.log2(n) + 0.5))

# n = int(input())
# for i in range(65):
#     k = 2 ** i - 1
#     for j in range(i+1, 65):
#         k *= 2
#     if k == n:
#         print(i)

# import math
# n = int(input())
# while  n%2 == 0:
#         n //= 2
#
# n_2 = n+1
# n_2_log = math.log2(n_2)
# print(int(n_2_log+0.5))