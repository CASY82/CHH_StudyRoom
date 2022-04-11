import sys

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n+1)]

edges = []
total_cost = 0

for _ in range(m):
    src, dest, cost = map(int, sys.stdin.readline().split())

    edges.append((cost, src, dest))

edges.sort()

def getParent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(m):
    cost, src, dest = edges[i]

    if getParent(parent, src) != getParent(parent, dest):
        unionParent(parent, src, dest)
        total_cost += cost

print(total_cost)