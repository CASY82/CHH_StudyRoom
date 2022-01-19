import sys

n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    needTree = 0

    for i in tree:
        if i > mid:
            needTree += i - mid

    if needTree < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)