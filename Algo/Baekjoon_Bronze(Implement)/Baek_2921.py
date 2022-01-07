import sys

n = int(sys.stdin.readline())
result = 0

for i in range(n+1):
    for j in range(i, i*2+1):
        result += j

print(result)