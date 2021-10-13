n = int(input())
result = []

for i in range(n):
    first, second, third = map(int, input().split())
    count = 0
    tmp = 0

    if first == second:
        tmp = first
        count += 1

    if second == third:
        tmp = second
        count += 1

    if third == first:
        tmp = third
        count += 1

    if count >= 2:
        result.append(10000 + (tmp * 1000))

    if count == 1:
        result.append(1000 + (tmp * 100))

    if count == 0:
        result.append(max(first, second, third) * 100)

print(max(result))


# set을 이용해서 중복을 없애는 방법이...
#
# def reward(n):
#     if len(set(n)) == 3:
#         return n[-1]*100
#     elif len(set(n)) == 2:
#         return 1000+n[1]*100
#     else:
#         return 10000 + n[0]*1000
# result = 0
# for _ in '-'*int(input()):
#     n = sorted(list(map(int, input().split())))
#     tmp = reward(n)
#     if result < tmp:
#         result = tmp
# print(result)