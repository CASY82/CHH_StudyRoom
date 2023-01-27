import sys

t = int(sys.stdin.readline())

#6까지는 직접 만들어서 풀어버리기로 결심
dp = [1, 1, 2, 2, 3, 3] + [0] * 100000

for i in range(6, 100001):
    # 서로 대칭이므로 해당 규칙이 된다.
    # i-2는 {1 + (x-2) + 1}
    # i-4는 {2 + (x-4) + 2}
    # i-6은 {3 + (x-6) + 3}
    # 즉 가운데에 대칭이 들어가며 추가되는 형식
    dp[i] = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009

for _ in range(t):
    num = int(sys.stdin.readline())

    print(dp[num])