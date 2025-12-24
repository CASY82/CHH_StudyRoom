import sys

n, m = map(int, sys.stdin.readline().split())
fish = list(map(int, sys.stdin.readline().split()))
buyer = []
res = 0
check = False

for _ in range(m):
    x, p = map(int, sys.stdin.readline().split())

    buyer.append([x, p])

buyer.sort(key=lambda x: -x[1])
fish.sort()

for i in range(m):
    for j in range(buyer[i][0]):
        if len(fish) > 0:
            res += buyer[i][1] * fish.pop()
        else:
            check = True
            break

    if check:
        break

print(res)