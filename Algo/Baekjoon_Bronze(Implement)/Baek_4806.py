import sys

cnt = 0

while True:
    sent = sys.stdin.readline().strip()

    if sent == "":
        break

    cnt += 1

print(cnt)