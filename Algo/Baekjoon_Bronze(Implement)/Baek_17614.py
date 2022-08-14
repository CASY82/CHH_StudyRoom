import sys

n = int(sys.stdin.readline())

result = 0
for i in range(1, n+1):
    tmp = str(i)

    result += tmp.count('3') + tmp.count('6') + tmp.count('9')

print(result)