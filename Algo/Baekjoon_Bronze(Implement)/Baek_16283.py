import sys

a, b, n, w = map(int, sys.stdin.readline().split())

check = False
cnt = 0

for i in range(1, n):
    if i + n - i == n and i * b + (n - i) * a == w:
        check = True
        if cnt == 0:
            goat = i
            lamb = n - i

        cnt += 1

if check and cnt == 1:
    print(lamb, goat)
else:
    print(-1)

# 다른 사람 풀이
# a, b, n, w = map(int, input().split())
# cnt = 0
# for i in range(1, n):
#     A = i
#     B = n - i
#     if A * a + B * b == w:
#         s = A
#         g = B
#         cnt += 1
#
# if cnt == 1:
#     print(s, g)
# else:
#     print(-1)