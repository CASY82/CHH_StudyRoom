import sys
from itertools import combinations

def find_target_sum(numbers, target, M):
    for combo in combinations(numbers, M):
        if sum(combo) == target:
            return True

    return False

n = int(sys.stdin.readline())

factorials = [1]
i = 1
fact = 1
res = "NO"

while n > fact:
    fact *= i
    factorials.append(fact)

    i += 1

for i in range(1, len(factorials) + 1):
    if find_target_sum(factorials, n, i):
        res = "YES"

print(res)

# 다른 사람 풀이
# able = [1]
# num = 1
# for i in range(1, 20):
#     num *= i
#     able.append(num)
#
# n = int(input())
# if n == 0:
#     print("NO")
#     exit()
# while able:
#     if able[-1] > n:
#         able.pop()
#     else:
#         n -= able.pop()
#
# if n == 0:
#     print("YES")
# else:
#     print("NO")
