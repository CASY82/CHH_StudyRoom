import sys

n = int(sys.stdin.readline())

wine = [0 for _ in range(10001)]
dp = [0 for _ in range(10001)]

for i in range(n):
    wine[i] = int(sys.stdin.readline())

dp[0] = wine[0]
dp[1] = max(wine[1], wine[0] + wine[1])
# 여기도 아래랑 똑같이 가야되는건데;;;; 잊었다
dp[2] = max(wine[1] + wine[2], wine[0] + wine[2], dp[1])

# dp[i-1]을 안해줘서 문제가 안풀리고 있었다... 마지막 전에걸 안마시는 경우, 해당 값이 최대인 경우를 가져와 줘야 했네....
for i in range(3, n):
    dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])

print(max(dp))