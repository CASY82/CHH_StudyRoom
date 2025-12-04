import sys

res = set()
tmp = set()

while True:
    ssn = sys.stdin.readline().strip()

    if ssn == "000-00-0000":
        break

    if ssn not in tmp:
        tmp.add(ssn)
    else:
        res.add(ssn)

res = list(res)
res.sort()

for name in res:
    print(name)