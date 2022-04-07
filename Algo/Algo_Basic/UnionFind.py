import sys

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

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a == b:
        return 1
    else:
        return 0

parent = [i for i in range(11)]

unionParent(parent, 1, 2)
unionParent(parent, 2, 3)
unionParent(parent, 3, 4)
unionParent(parent, 5, 6)
unionParent(parent, 6, 7)
unionParent(parent, 7, 8)

print("1 과 5는 연결?", findParent(parent, 1, 5))

unionParent(parent, 1, 5)
print("1 과 5는 연결?", findParent(parent, 1, 5))