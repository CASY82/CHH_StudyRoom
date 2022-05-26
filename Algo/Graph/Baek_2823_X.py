import sys

r, c = map(int, sys.stdin.readline().split())
city = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for _ in range(r):
    city.append(list(sys.stdin.readline().strip()))

for i in range(r):
    for j in range(c):
        if city[i][j] == ".":
            cnt = 0
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]

                if 0 <= nx < c and 0 <= ny < r:
                    if city[ny][nx] == ".":
                        cnt += 1

            if cnt < 2:
                print(1)
                exit()

print(0)