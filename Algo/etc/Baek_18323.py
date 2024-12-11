import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

tmp = [0] * n
res = []

for start in range(nums[0], 0, -1):
    check = True
    tmp[0] = start
    tmp[1] = nums[0] - start
    for i in range(1, n - 1):
        tmp[i + 1] = nums[i] - tmp[i]

    for k in range(1, n + 1):
        if k not in tmp:
            check = False
            break

    if check:
        res = tmp.copy()

print(*res)

# 다른 사람 풀이
"""
It is possible to construct sequence a given sequence b and the first term in a, a1.

let a1 = 1
begin building sequence a.
if any term is invalid, then the whole sequence is invalid, and we move on
if all terms are valid, then we print
"""
#
# N = int(input())
# b = list(map(int, input().split()))
#
# for a1 in range(1, N + 1):
#     a = [a1]
#     good = True
#
#     for i in range(N - 1):
#         next_a = b[i] - a[i]
#         if next_a < 1 or next_a > N or next_a in a:
#             good = False
#             break
#         a.append(next_a)
#
#     if good:
#         print(*a)