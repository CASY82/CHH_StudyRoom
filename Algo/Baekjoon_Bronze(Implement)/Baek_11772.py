import sys

n = int(sys.stdin.readline())

result = 0

for _ in range(n):
    numb = sys.stdin.readline().strip()

    tmp = int(numb[:-1]) ** int(numb[-1])

    result += tmp

print(result)