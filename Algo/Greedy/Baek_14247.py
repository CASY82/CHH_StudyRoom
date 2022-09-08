import sys
from collections import deque

n = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
grow = list(map(int, sys.stdin.readline().split()))
result = 0

tmp = []

for seq in range(n):
    tmp.append((tree[seq], grow[seq]))

tmp.sort(key= lambda x: x[1])
tmp = deque(tmp)

for i in range(n):
    tree_one, grows = tmp.popleft()

    result += tree_one + grows * i

print(result)