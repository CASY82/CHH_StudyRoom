#숫자 카드 게임

#min을 이용한 풀이

n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)

print(result)

#다른 풀이
# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#
#     min_value = 10001
#
#     for a in data:
#         min_value = min(min_value, a)
#
#     result = max(result, min_value)
#
# print(result)


