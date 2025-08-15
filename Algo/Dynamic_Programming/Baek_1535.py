import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

CAP = 99
dp = [0] * (CAP + 1)

for l, j in zip(L, J):
    for w in range(CAP, l - 1, -1):
        dp[w] = max(dp[w], dp[w - l] + j)

print(max(dp))