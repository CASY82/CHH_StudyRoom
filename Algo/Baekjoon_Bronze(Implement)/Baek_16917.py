import sys

a, b, c, x, y = map(int, sys.stdin.readline().split())

# 총 4가지 케이스
case1 = y * c * 2 + abs(x - y) * a # 양반 후반이 저렴하고, 후라이드를 더 구매 하는 경우
case2 = x * c * 2 + abs(y - x) * b # 양반 후반이 저렴하고, 양념을 더 구매 하는 경우
case3 = y * b + x * a # 각자 구매가 더 저렴한 경우
case4 = max(x, y) * c * 2 # 양반 후반으로 전부 구매하는 경우

# if a + b > c * 2:
#     if x > y:
#         res += y * c * 2
#         res += (x - y) * a
#     else:
#         res += x * c * 2
#         res += (y - x) * b
# else:
#     res += y * b + x * a

print(min(case1, case2, case3, case4))