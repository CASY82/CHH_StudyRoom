import sys

taebo = sys.stdin.readline().strip()

check = taebo.split('0')
result = []

for i in range(2):
    result.append(check[i].count('@'))

print(*result)