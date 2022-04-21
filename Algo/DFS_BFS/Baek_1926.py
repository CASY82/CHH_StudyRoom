import sys
sys.setrecursionlimit(3000000)

n, m = map(int, sys.stdin.readline().split())
picture = []
cnt = 0
big = 0

for _ in range(n):
    picture.append(list(map(int, sys.stdin.readline().split())))

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False

    if picture[y][x] == 1:
        picture[y][x] = 2
        big_cnt[0] += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True

    return False

for i in range(n):
    for j in range(m):
        big_cnt = [0]
        if dfs(j, i):
            cnt += 1

        if big_cnt[0] > big:
            big = big_cnt[0]

print(cnt)
print(big)