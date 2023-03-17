import sys
sys.setrecursionlimit(300000)

n = int(sys.stdin.readline())
quad_tree = []

for _ in range(n):
    quad_tree.append(list(map(int, sys.stdin.readline().strip())))

def divideConquer(x, y, n):
    # 쪼개진 부분에 속하는 원소가 동일한가?
    check = quad_tree[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != quad_tree[i][j]:
                check = -1
                break

    # 즉 해당 사분면에 다른 원소가 존재할 경우
    if check == -1:
        print("(", end="")
        # 크기 축소
        n //= 2
        # 순서 중요
        divideConquer(x, y, n)  # 1사분면
        divideConquer(x, y + n, n) # 2사분면
        divideConquer(x + n, y, n) # 3사분면
        divideConquer(x + n, y + n, n) # 4사분면
        print(")", end="")
    # 1만 모인 사분면이라면?
    elif check == 1:
        print(1, end="")
    # 나머지 0 처리
    else:
        print(0, end="")

divideConquer(0, 0, n)