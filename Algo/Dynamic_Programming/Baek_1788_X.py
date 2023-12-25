# import sys
#
# n = int(sys.stdin.readline())
#
# dp = [0 for _ in range(1000001)]
#
# dp[0] = 0
# dp[1] = 1
#
# if n >= 0:
#     for i in range(2, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
#
# else:
#     n = abs(n)
#     dp[2] = -1
#     for i in range(3, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
#
# print(dp[2])

import sys

n = int(sys.stdin.readline())
s = [0, 1]

#음수여도 기본 규칙은 동일. 단지 짝수번째 애들은 음수로 표기된다.
for i in range(2, abs(n) + 1):
    s.append((s[i - 1] + s[i - 2]) % 1000000000)
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)
print(s[abs(n)])