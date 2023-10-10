import sys

susic = sys.stdin.readline().strip().split()

tmp = susic[:3]
if eval("".join(tmp)) == int(susic[-1]):
    print("YES")
else:
    print("NO")