import sys

n = int(sys.stdin.readline())

boxes = list(map(int, sys.stdin.readline().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 이렇게 풀면 안되네..
# import sys
#
# n = int(sys.stdin.readline())
# boxes = list(map(int, sys.stdin.readline().split()))
# result = 1
# now = boxes[0]
#
# for i in range(1, n):
#     if now < boxes[i]:
#         result += 1
#         now = boxes[i]
#
# print(result)