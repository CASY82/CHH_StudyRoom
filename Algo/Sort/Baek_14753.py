import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

print(max(numbers[-1] * numbers[-2] * numbers[-3], numbers[-1] * numbers[-2], numbers[0] * numbers[1], numbers[0] * numbers[1] * numbers[-1]))