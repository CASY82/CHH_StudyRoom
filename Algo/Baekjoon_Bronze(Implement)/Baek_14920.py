import sys

n = int(sys.stdin.readline())
last_num = 1

while n > 1:
    last_num += 1
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n // 2

print(last_num)