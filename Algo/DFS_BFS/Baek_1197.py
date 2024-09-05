import sys
sys.setrecursionlimit(500000)

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

v, e = map(int, sys.stdin.readline().split())
parent = [i for i in range(v + 1)]

edges = []
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())

    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b = edges[i]

    if getParent(parent, a) != getParent(parent, b):
        unionParent(parent, a, b)
        total_cost += cost

print(total_cost)