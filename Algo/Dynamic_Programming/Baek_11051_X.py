import sys

n, k = map(int, sys.stdin.readline().split())

#직접 조합을 구현한다.
def bino_coef(n, r):
    num_arr = [[0 for _ in range(r+1)] for _ in range(n+1)]

    for i in range(n+1):
        num_arr[i][0] = 1

    # 조합 공식에서 nCr 중 n == r이면 전부 1임
    for j in range(r+1):
        num_arr[j][j] = 1

    #DP 인 이유
    for i in range(1, n+1):
        for j in range(1, r+1):
            num_arr[i][j] = (num_arr[i-1][j] + num_arr[i-1][j-1]) % 10007

    return num_arr[n][r]

print(bino_coef(n, k))