# c, n = map(int, input().split())
# city = []
# dp = [float('inf') for i in range(20001)]
# new_max = 0
#
# for _ in range(n):
#     city.append(list(map(int, input().split())))
#
# # print(city)
#
# for i in range(n):
#     dp[city[i][1]] = city[i][0]
#
# #'적어도'때문에 넣게된 부분
# for i in range(n):
#     if c//city[i][1] > new_max:
#         new_max = (c//city[i][0] + 1) * city[i][1]
#
# #곱을 하다보니 배열 범위를 넘어간다
# if new_max > 20000:
#     new_max = 20000
#
# # print(new_max)
#
# for i in range(n):
#     for j in range(2, new_max+1):
#         if dp[j] > dp[j-city[i][1]] + city[i][0]:
#             dp[j] = dp[j-city[i][1]] + city[i][0]
#
# # print(dp)
#
# result=float('inf')
#
# for i in range(c, new_max+1):
#     result = min(dp[i], result)
#
# print(result)

#동적프로그래밍... 아직 너무 부족하다 점화식 세우는 연습이 더 필요할것 같다.
import sys
sys.setrecursionlimit(10000)

c, n = map(int, input().split())
city = []
dp = [0 for i in range(1001)]

def dp_city(c, n):
    miner = 100 * 1000
    cost = 0

    if c <= 0:
        return 0
    elif dp[c] > 0:
        return dp[c]
    else:
        for i in range(n):
            cost = dp_city(c-city[i][1], n) + city[i][0]
            miner = cost if cost < miner else miner

        dp[c] = miner

        return miner



for _ in range(n):
    city.append(list(map(int, input().split())))

print(dp_city(c,n))