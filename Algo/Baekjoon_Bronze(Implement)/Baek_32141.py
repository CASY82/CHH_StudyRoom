import sys

n, h = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

cards.sort()
res = 0

for i in range(n):
    if h - cards[i] <= 0:
        res += 1
        h -= cards[i]
        break

    h -= cards[i]
    res += 1

if h > 0:
    res = -1

print(res)

# 다른 사람
# N, H = map(int, input().split())
# hunt = list(map(int, input().split()))
#
# for i in range(len(hunt)):
#     H = H - hunt[i]
#     if H <= 0:
#         print(i+1)
#         break
#
# if H > 0:
#     print(-1)