import sys

n, m = map(int, sys.stdin.readline().split())
money = list(map(int, sys.stdin.readline().split()))

person_get_money = [0 for _ in range(n + m)]

for i in range(n):
    div = list(map(int, sys.stdin.readline().split()))
    money[i] -= sum(div)
    person_get_money[i] += money[i]
    for j in range(n + m):
        person_get_money[j] += div[j]

print(*person_get_money)

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# arr = list(map(int, input().split())) + [0 for _ in range(m)]
#
# for i in range(n):
#     now = list(map(int, input().split()))
#     for j in range(m+n):
#         arr[i] -= now[j]
#         arr[j] += now[j]
#
# print(" ".join(map(str, arr)))