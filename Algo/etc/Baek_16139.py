# import sys
#
# s = sys.stdin.readline().strip()
# q = int(sys.stdin.readline())
#
# n = len(s)
#
# prefix = [[0] * n for _ in range(26)]
#
# prefix[ord(s[0]) - 97][0] = 1
#
# for i in range(1, n):
#     for j in range(26):
#         prefix[j][i] = prefix[j][i - 1]
#     prefix[ord(s[i]) - 97][i] += 1
#
# for _ in range(q):
#     alpha, l, r = input().split()
#     l = int(l)
#     r = int(r)
#     idx = ord(alpha) - 97
#
#     if l == 0:
#         print(prefix[idx][r])
#     else:
#         print(prefix[idx][r] - prefix[idx][l - 1])

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

S = input().strip()
q = int(input())

# 알파벳별 등장 위치 저장
where = [[] for _ in range(26)]
for i, ch in enumerate(S):
    where[ord(ch) - 97].append(i)

out_lines = []
for _ in range(q):
    a, l, r = input().split()
    l = int(l); r = int(r)
    arr = where[ord(a) - 97]
    # [l, r] 범위 안의 개수 = 오른쪽 경계 인덱스 - 왼쪽 경계 인덱스
    cnt = bisect_right(arr, r) - bisect_left(arr, l)
    out_lines.append(str(cnt))

print("\n".join(out_lines))
