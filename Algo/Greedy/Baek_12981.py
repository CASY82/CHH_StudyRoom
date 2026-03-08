# 공 포장하기
R, G, B = map(int, input().split())

INF = 10**9

dp = [[[INF] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]
dp[0][0][0] = 0

for r in range(R + 1):
    for g in range(G + 1):
        for b in range(B + 1):
            cur = dp[r][g][b]
            if cur == INF:
                continue

            # 1개
            if r + 1 <= R:
                dp[r + 1][g][b] = min(dp[r + 1][g][b], cur + 1)
            if g + 1 <= G:
                dp[r][g + 1][b] = min(dp[r][g + 1][b], cur + 1)
            if b + 1 <= B:
                dp[r][g][b + 1] = min(dp[r][g][b + 1], cur + 1)

            # 2개 같은 색
            if r + 2 <= R:
                dp[r + 2][g][b] = min(dp[r + 2][g][b], cur + 1)
            if g + 2 <= G:
                dp[r][g + 2][b] = min(dp[r][g + 2][b], cur + 1)
            if b + 2 <= B:
                dp[r][g][b + 2] = min(dp[r][g][b + 2], cur + 1)

            # 2개 다른 색
            if r + 1 <= R and g + 1 <= G:
                dp[r + 1][g + 1][b] = min(dp[r + 1][g + 1][b], cur + 1)
            if r + 1 <= R and b + 1 <= B:
                dp[r + 1][g][b + 1] = min(dp[r + 1][g][b + 1], cur + 1)
            if g + 1 <= G and b + 1 <= B:
                dp[r][g + 1][b + 1] = min(dp[r][g + 1][b + 1], cur + 1)

            # 3개 같은 색
            if r + 3 <= R:
                dp[r + 3][g][b] = min(dp[r + 3][g][b], cur + 1)
            if g + 3 <= G:
                dp[r][g + 3][b] = min(dp[r][g + 3][b], cur + 1)
            if b + 3 <= B:
                dp[r][g][b + 3] = min(dp[r][g][b + 3], cur + 1)

            # 3개 모두 다른 색
            if r + 1 <= R and g + 1 <= G and b + 1 <= B:
                dp[r + 1][g + 1][b + 1] = min(dp[r + 1][g + 1][b + 1], cur + 1)

print(dp[R][G][B])

# 다른 사람 풀이
# R, G, B = map(int, input().split())
# MIN = min(R,G,B)
# result = MIN
# R -= MIN
# G -= MIN
# B -= MIN
# # 같은 공이 2개 남아 있는 경우
# result += R//3 + G//3 + B//3
# R %= 3
# G %= 3
# B %= 3
# # 같은 공이 2개 남아 있는 경우
# if R == 2:
#   result += 1
#   R = 0
# if G == 2:
#   result += 1
#   G = 0
# if B == 2:
#   result += 1
#   B = 0
# # 공이 1개 혹은 두 종류의 공이 1개씩 있는 경우
# if R+G+B > 0:
#   result += 1
# print(result)