import sys
import math

num = int(sys.stdin.readline())

n = 120

array = [True for i in range(n + 1)]
decimal = []
decimal_mul = []

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        decimal.append(i)

for i in range(len(decimal) - 1):
    decimal_mul.append(decimal[i] * decimal[i + 1])

decimal_mul.sort()

for dec in decimal_mul:
    if dec > num:
        print(dec)
        break