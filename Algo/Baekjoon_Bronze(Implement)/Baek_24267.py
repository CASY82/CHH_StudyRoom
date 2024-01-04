import sys

n = int(sys.stdin.readline())

print(n * (n - 1) * (n - 2) // 6)
print(3)

# sum = 0
# a = [1 for _ in range(n + 1)]
# cnt = 0

# 시그마 전개 식
# for i in range(1, n - 1):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n + 1):
#             sum += (a[i] * a[j] * a[k])
#             print(i, j, k)
#             cnt += 1
#
# print(cnt)