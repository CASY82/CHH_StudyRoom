import sys
sys.setrecursionlimit(300000)

num = []
result = set()


for _ in range(5):
    num.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y, cnt, numStr):
    if x < 0 or y < 0 or x >= 5 or y >= 5:
        return False

    if cnt == 5:
        numStr += str(num[y][x])
        result.add(numStr)
        return True

    numStr += str(num[y][x])
    dfs(x+1, y, cnt + 1, numStr)
    dfs(x-1, y, cnt + 1, numStr)
    dfs(x, y+1, cnt + 1, numStr)
    dfs(x, y-1, cnt + 1, numStr)

    return False

for i in range(5):
    for j in range(5):
        dfs(j, i, 0, "")

print(len(result))