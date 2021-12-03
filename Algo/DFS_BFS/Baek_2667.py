n = int(input())
danzi = []

for _ in range(n):
    danzi.append(list(map(int, input())))

def dfs(x, y):

    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False

    if danzi[x][y] == 1:
        danzi[x][y] = 0
        record.append(1)

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False

#개수 세는 것은 약간 아이디어를 얻어서 풀었다... 그래도 성공!
result = 0
count = []
for i in range(n):
    for j in range(n):
        record = []
        if dfs(i, j):
            result += 1
            count.append(sum(record))

count.sort()
print(result)
for i in count:
    print(i)