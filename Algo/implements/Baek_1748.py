import sys

n = int(sys.stdin.readline())
result = 0

length = len(str(n))

for i in range(1, length+1):
    if length > i:
        result += (9 * (10 ** (i-1))) * i
    else:
        result += (n - (10 ** (i-1)) + 1) * i

print(result)