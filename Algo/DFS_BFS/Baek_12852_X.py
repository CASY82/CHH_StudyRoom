# 메모리 초과가 나올것 같다.
# import sys
# from collections import deque
# n = int(sys.stdin.readline())
# cnt = 0
# result = 0
# queue = deque([(n, 0)])
# check = [0 for i in range(1000000)]
#
# while queue:
#     print(queue)
#     num, cnt = queue.popleft()
#
#     if num == 1:
#         result = cnt
#         break
#
#     if num % 3 == 0:
#         queue.append((num // 3, cnt + 1))
#
#     if num % 2 == 0:
#         queue.append((num // 2, cnt + 1))
#
#     queue.append((num - 1, cnt + 1))
#
# print(cnt)

# 일단 개수는 맞게 나오나... 단계 출력이 어렵다... top down이라 그런가...?
# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
# result = 0
# queue = deque([n])
# check = [0 for i in range(20)]
#
# while queue:
#     num = queue.popleft()
#
#     print(num)
#     if num == 1:
#         print(check[num])
#         break
#
#     if num % 3 == 0:
#         check[num // 3] = check[num] + 1
#         queue.append(num // 3)
#
#     if num % 2 == 0:
#         check[num // 3] = check[num] + 1
#         queue.append(num // 2)
#
#     queue.append(num - 1)
#     check[num - 1] = check[num] + 1

import sys
from collections import deque

n = int(sys.stdin.readline())
result = []
queue = deque()
queue.append([n])

# 앞에 구현한 코드에서는 개수만 세도록 되어있었다면, 이번 코드에서는 아예 수 자체를 넣고 빼는 방식;; 생각도 못했다.
while queue:
    num = queue.popleft()
    x = num[0]

    if x == 1:
        result = num
        break

    if x % 3 == 0:
        queue.append([x // 3] + num)

    if x % 2 == 0:
        queue.append([x // 2] + num)

    queue.append([x - 1] + num)

print(len(result) - 1)
print(*result[::-1])

#본래의 DP로 푸는 방법
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dp = [[0, []] for _ in range(n + 1)]
# dp[1][0] = 0
# dp[1][1] = [1]
#
# for i in range(2, n + 1):
#     dp[i][0] = dp[i-1][0] + 1
#     dp[i][1] = dp[i-1][1] + [i]
#     if i % 3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 3][0] + 1
#         dp[i][1] = dp[i // 3][1] + [i]
#     if i % 2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
#         dp[i][0] = dp[i // 2][0] + 1
#         dp[i][1] = dp[i // 2][1] + [i]
#
# print(dp[n][0])
# print(*reversed(dp[n][1]))