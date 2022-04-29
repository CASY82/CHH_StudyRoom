import sys

n, k = map(int, sys.stdin.readline().split())

backpack_weight = [0]
backpack_val = [0]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    backpack_weight.append(w)
    backpack_val.append(v)

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif backpack_weight[i] <= j:
            # 현재 선택된 물건 무게를 뺀 무게 중 가장 최댓값 + 현재 넣을 물건 무게 vs 이전에 등록된 같은 무게 값
            dp[i][j] = max(backpack_val[i] + dp[i-1][j - backpack_weight[i]], dp[i-1][j])
        elif backpack_weight[i] > j:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

# 다른사람 풀이
# n, k = input().split()
# n = int(n)
# k = int(k)
#
# weight_item = []
# value_item = []
#
# for i in range(n):
#     w, v = input().split()
#
#     weight_item.append(int(w))
#     value_item.append(int(v))
#
# table = [0] * (k + 1)
#
# for i in range(n):
#     for j in range(k, weight_item[i] - 1, -1):
#         table[j] = max(table[j], table[j - weight_item[i]] + value_item[i])
#
# print(table[k])
