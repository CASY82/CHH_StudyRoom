import sys

dancer = set()
n = int(sys.stdin.readline())

dancer.add("ChongChong")

for _ in range(n):
    a, b = sys.stdin.readline().strip().split()

    if (a in dancer) or (b in dancer):
        dancer.add(a)
        dancer.add(b)

print(len(dancer))