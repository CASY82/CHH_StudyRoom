import sys

n, m = map(int, sys.stdin.readline().split())

def getParent(parent, x):
    if parent[x] == x:
        return x

    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    # 파티에서 둘다 알고있는 사람인 경우 넘어감
    if a in know and b in know:
        return

    # 한명만 아는경우 아는사람으로 연결
    if a in know:
        parent[b] = a

    elif b in know:
        parent[a] = b

    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

parent = [i for i in range(n+1)]
know = list(map(int, sys.stdin.readline().split()))[1:]
parties = []
cnt = 0

for _ in range(m):
    party_info = list(map(int, sys.stdin.readline().split()))
    party_len = party_info[0]
    party = party_info[1:]

    for i in range(party_len - 1):
        unionParent(parent, party[i], party[i+1])

    parties.append(party)

for j in parties:
    for k in range(len(j)):
        if getParent(parent, j[k]) in know:
            break
    else:
        cnt += 1

print(cnt)