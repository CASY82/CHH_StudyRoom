# 최장 길이 구하는 함수
# 재귀 방법 (호출 횟수가 많으므로 시간 초과 가능성 up)

# def LCS(x, y, m, n):
#     if m == 0 and n == 0:
#         return 0
#     elif x[m-1] == y[n-1]:
#         return LCS(x, y, m-1, n -1) + 1
#     else:
#         return max(LCS(x, y, m-1, n), LCS(x, y, m, n-1))
#

# DP 이용 방법

x = input()
y = input()

c = [[0] * (len(y)+1) for _ in range(len(x)+1)]

def LCS(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return c[m][n]

print(LCS(len(x), len(y)))