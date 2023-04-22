import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(n):
    expiration_date = sys.stdin.readline().strip()

    expiration_date = expiration_date.replace("D-", "")

    if int(expiration_date) <= 90:
        cnt += 1

print(cnt)