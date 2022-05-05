import sys

n = int(sys.stdin.readline())
cnt = 0

while n > 1:
    if n % 2 == 0:
        n //= 2
    else:
        n += 1

    cnt += 1

print(cnt)