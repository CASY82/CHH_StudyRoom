import sys

n = int(sys.stdin.readline())
comedian = []

for i in range(n):
    comedian.append(int(sys.stdin.readline()))

if max(comedian) == comedian[0]:
    print('S')
else:
    print('N')