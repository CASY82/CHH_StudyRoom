import sys

n = int(sys.stdin.readline())

haligali = dict()

for _ in range(n):
    fruit, cnt = sys.stdin.readline().strip().split()

    if fruit not in haligali:
        haligali[fruit] = int(cnt)
    else:
        haligali[fruit] += int(cnt)

if 5 in haligali.values():
    print("YES")
else:
    print("NO")