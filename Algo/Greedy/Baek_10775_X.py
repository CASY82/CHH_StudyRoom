import sys

def getParent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionFind(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

docking_gate = dict()
airplane = []
cnt = 0

for i in range(g+1):
    docking_gate[i] = i

for j in range(p):
    airplane.append(int(sys.stdin.readline()))

for number in airplane:
    x = getParent(docking_gate, number)

    if x == 0:
        break

    unionFind(docking_gate, x, x-1)
    cnt += 1

print(cnt)
# print(docking_gate)
# 즉 부모를 결합시키면서 0으로 최종 유도하는 방식을 이용한 것이라는 것을 깨달을 수 있었음 최종적으로 -1해서 0이 나오면 더이상 공간이 없다는 뜻이됨