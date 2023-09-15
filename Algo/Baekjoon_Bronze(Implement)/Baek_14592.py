import sys
n = int(sys.stdin.readline())

array = []

for i in range(n):
    s, c, l = map(int, sys.stdin.readline().split())
    array.append((s, c, l, i+1))

array.sort(key=lambda x : (-x[0], x[1], x[2]))

print(array[0][-1])