import sys

a, b, c = map(int, sys.stdin.readline().split())

average = (a + b + c) // 3

result = 0

result += (average - a)
b -= (average - a)
result += (average - b)

print(result)