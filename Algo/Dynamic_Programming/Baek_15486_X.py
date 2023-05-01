import sys

n = int(sys.stdin.readline())
days = []
dp = [0 for i in range(n+1)]

# 데이터 입력
for _ in range(n):
    ti, pi = map(int, sys.stdin.readline().split())

    days.append((ti, pi))

max_val = 0

for i in range(n):
    # 매번 i번째 일에 max값이 될 수 있는 금액을 갱신(지금까지 가지고 있던 max_val이 더 큰지, 아니면 이미 dp가 가지고 있던 값이 더 큰지)
    max_val = max(max_val, dp[i])

    # 내가 끝나는 날짜 더했는데, 퇴직 날짜 넘어간 것이라면 계산 안함
    if i + days[i][0] > n:
        continue

    # dp 값 갱신(max_val값과 당일의 pay를 더한 값과, 다음 dp에서 이미 계산되어 있는 pay를 비교해서 더 큰 값을 저장)
    # 여기서 다음 날짜를 미리 계산 하는 방식 사용
    dp[i + days[i][0]] = max(max_val + days[i][1], dp[i + days[i][0]])

print(max(dp))