import sys

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

a = numbers[0]
b = numbers[1]
abc_total = numbers[-1]
c = abc_total - a - b

print(a, b, c)