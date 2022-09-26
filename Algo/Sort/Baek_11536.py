import sys

n = int(sys.stdin.readline())
name = []

for _ in range(n):
    name.append(sys.stdin.readline().strip())

inc = name.copy()
dec = name.copy()

inc.sort()
dec.sort(reverse=True)

if inc == name:
    print("INCREASING")
elif dec == name:
    print("DECREASING")
else:
    print("NEITHER")