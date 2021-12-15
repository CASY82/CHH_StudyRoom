import sys

n = int(sys.stdin.readline())
result = 1

for i in range(1, n+1):
    result *= i

result = str(result)
cnt = 0
for i in range(len(result)-1, 0, -1):
    if result[i] != '0':
        break
    else:
        cnt += 1

print(cnt)