import sys

susic = list(sys.stdin.readline().strip().split())

tmp = eval("".join(susic[0:3]))
if tmp == int(susic[-1]):
    print("YES")
else:
    print("NO")