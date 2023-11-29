import sys

n = int(sys.stdin.readline())

condo = []

costs = 10001
result = 0

for _ in range(n):
    d, c = map(int, sys.stdin.readline().split())

    condo.append([d, c])

condo.sort()

# 그냥 정렬을 하면 x[0] 기준 정렬 이때, 거리가 제일 가까운녀석중 제일 싼놈이 condo[0]로 오게 됨
# 이 가격을 tmp에 저장하고 이후 for문을 돌면 거리가 멀어지지만 제일 가까운놈보다 싼녀석을 search하게 됨
# 그 콘도도 후보로 넣을 수 있으므로 해당 경우에도 result + 1
for check in condo:
    tmp = check[1]
    if tmp < costs:
        costs = tmp
        result += 1

print(result)