import sys

n = int(sys.stdin.readline())

length = []
result = -1

for _ in range(n):
    length.append(int(sys.stdin.readline()))

length.sort(reverse=True)

for i in range(n-2):
    if length[i] < length[i + 1] + length[i + 2]:
        result = length[i] + length[i + 1] + length[i + 2]
        break

print(result)