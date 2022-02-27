import sys

n, m = map(int, sys.stdin.readline().split())
war = []
counter = [0]
resultB = 0
resultW = 0

for _ in range(m):
    war.append(list(sys.stdin.readline().strip()))

def dfs(x, y, peer):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if war[y][x] == peer:
        counter[0] += 1
        war[y][x] = 'K'
        dfs(x + 1, y, peer)
        dfs(x - 1, y, peer)
        dfs(x, y + 1, peer)
        dfs(x, y - 1, peer)
        return True

    return False

for i in range(m):
    for j in range(n):
        if dfs(j, i, 'B'):
            resultB += counter[0] * counter[0]
            counter[0] = 0

        if dfs(j, i, 'W'):
            resultW += counter[0] * counter[0]
            counter[0] = 0

print(resultW, resultB)