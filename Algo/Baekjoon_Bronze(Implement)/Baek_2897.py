# 몬스터 트럭
import sys

r, c = map(int, sys.stdin.readline().split())
res = [0, 0, 0, 0, 0] # 0, 1, 2, 3, 4
parking = []

for _ in range(r):
    parking.append(list(sys.stdin.readline().strip()))

# 각 행에서 . 으로 시작하면 아래, 오른쪽, 오른쪽 대각선 이렇게 네 부분만 확인
checker = [(0, 0), (1, 0), (0, 1), (1, 1)]

for i in range(r - 1):
    for j in range(c - 1):
        cnt = 0
        check = True
        if parking[i][j] == "#":
            continue
        else:
            for x, y in checker:
                if parking[i + y][j + x] == "#":
                    check = False
                    break
                elif parking[i + y][j + x] == "X":
                    cnt += 1

            if check:
                res[cnt] += 1

for i in res:
    print(i)