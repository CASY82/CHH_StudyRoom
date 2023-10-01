import sys

n = int(sys.stdin.readline())
cnt = 0
cat = 0

while True:
    if cat == n:
        break

    if cat == 0:
        cat += 1
        cnt += 1
        continue

    if cat < n <= cat * 2:
        cnt += 1
        break

    cat *= 2
    cnt += 1

print(cnt)