import sys

n = int(sys.stdin.readline())
tmp = []

for index in range(1, n + 1):
    j, p = map(int, sys.stdin.readline().split())

    tmp.append([index, j/p, p])

tmp.sort(key=lambda x:x[1])

print(tmp[-1][2] + tmp[-2][2] + tmp[-3][2])
print(tmp[-1][0])
print(tmp[-2][0])
print(tmp[-3][0])