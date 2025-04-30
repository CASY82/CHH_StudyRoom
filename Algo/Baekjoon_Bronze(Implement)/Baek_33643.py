import sys

n = int(sys.stdin.readline())
items = set()
res = []

for _ in range(n):
    items.add(sys.stdin.readline().strip())

for check in ["keys", "phone", "wallet"]:
    if check not in items:
        res.append(check)

if len(res) == 0:
    print("ready")
else:
    for an in res:
        print(an)