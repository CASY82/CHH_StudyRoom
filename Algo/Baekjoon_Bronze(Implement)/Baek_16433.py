# 주디와 당근농장
import sys
sys.setrecursionlimit(100000)

n, r, c = map(int, sys.stdin.readline().split())

array = [["." for _ in range(n)] for _ in range(n)]
dr = [1, 1, -1, -1]
dc = [1, -1, 1, -1]

def logic(r, c):
    for i in range(4):
        if 0 <= r + dr[i] < n and 0 <= c + dc[i] < n:
            if array[r + dr[i]][c + dc[i]] == ".":
                array[r + dr[i]][c + dc[i]] = "v"
                logic(r + dr[i], c + dc[i])

array[r - 1][c - 1] = "v"
logic(r - 1, c - 1)

for j in range(n):
    for k in range(n):
        print(array[j][k], end="")
    print()