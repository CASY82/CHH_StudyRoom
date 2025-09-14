# import sys
#
# isbn = sys.stdin.readline().strip()
# tmp = 0
# index = 0
#
# for i in range(len(isbn)):
#     if isbn[i] != "*":
#         if i % 2 == 1:
#             tmp += int(isbn[i]) * 3
#         else:
#             tmp += int(isbn[i])
#
#     else:
#         index = i
#
# tmp2 = tmp % 10
#
# if index % 2 == 1:
#     for i in range(1, 10):
#         if (i * 3) % 10 == 0:
#             res = i
#             break
# else:
#     res = 10 - tmp2
#
# print(res)

import sys

isbn = sys.stdin.readline().strip()

tmp = 0
idx = isbn.index('*')

for i, ch in enumerate(isbn):
    if ch == '*':
        continue
    d = int(ch)
    tmp += d * (3 if i % 2 == 1 else 1)

# 누락된 자리의 가중치
w = 3 if idx % 2 == 1 else 1
inv = 7 if w == 3 else 1  # 3의 mod 10 역원은 7, 1의 역원은 1

# x ≡ -tmp * inv (mod 10)
res = (-tmp * inv) % 10
print(res)
