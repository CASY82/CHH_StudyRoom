import sys

number = list(map(int, sys.stdin.readline().split()))

number.sort()

if number[0] + number[1] <= number[2]:
    number[2] = number[0] + number[1] - 1

print(sum(number))