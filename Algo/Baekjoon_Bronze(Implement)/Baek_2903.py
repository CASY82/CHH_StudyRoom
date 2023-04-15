import sys

start = 2
n = int(sys.stdin.readline())
result = [0]

def func(input_num):
    next = (input_num-1) + input_num
    result[0] = next ** 2
    return next

for i in range(n):
    start = func(start)

print(result[0])