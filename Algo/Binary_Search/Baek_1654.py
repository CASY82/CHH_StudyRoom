import sys

n, k = map(int, sys.stdin.readline().split())
lanlen = []

for _ in range(n):
    lanlen.append(int(sys.stdin.readline()))

#일단 길이가 가장 긴 랜선을 기준으로
start = 0
end = max(lanlen)

#항상 쓰던 그 이분탐색을 이용하여
while start <= end:
    mid = (start + end) // 2
    #개수를 세야지
    total_cnt = 0

    #와 end가 1인경우는 생각도 못했다;
    if mid == 0:
        break

    #각 데이터에서 mid값을 나눠서 데이터를 더한 다음
    for i in lanlen:
        total_cnt += i // mid

    #개수가 적네? 그럼 범위를 줄여서 길이를 줄여 개수를 늘리고
    if total_cnt < k:
        end = mid - 1
    #개수가 많네? 그럼 범위를 늘려서 길이를 길게 하여 개수를 줄인다.
    else:
        start = mid + 1

#그래서 마지막 end출력하면 되는데 이거 왜 end출력인가...?(경험적 예상에 의한 답 때려 맞추기라 너무 화난다)
print(end)