# IOIOI

# 시간 초과
# import sys
# import re
#
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# s = sys.stdin.readline().strip()
#
# origin_model = "IOI"
#
# for _ in range(n - 1):
#     origin_model = origin_model + "OI"
#
# cnt = sum(1 for _ in re.finditer(r'(?={})'.format(origin_model), s))
#
# print(cnt)

import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

cnt = 0
k = 0
i = 0

while i < m - 2:
    if s[i] == 'I' and s[i + 1] == 'O' and s[i + 2] == 'I':
        k += 1
        if k >= n:
            cnt += 1
        i += 2
    else:
        k = 0
        i += 1

print(cnt)