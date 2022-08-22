import sys

n, k = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
diff = []

height.sort()

for i in range(len(height)-1):
    diff.append(height[i+1] - height[i])

diff.sort()

for _ in range(k-1):
    diff.pop()

print(sum(diff))