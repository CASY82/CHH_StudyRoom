import sys

n = int(sys.stdin.readline())

origin = list(sys.stdin.readline().strip())
result = list(sys.stdin.readline().strip())

compare = origin[:]

for _ in range(n):
    for i in range(len(origin)):
        if compare[i] == "1":
            compare[i] = "0"
        else:
            compare[i] = "1"

if compare == result:
    print("Deletion succeeded")
else:
    print("Deletion failed")