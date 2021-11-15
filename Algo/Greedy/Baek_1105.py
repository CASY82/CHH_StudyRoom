l, r = input().split()
count = 0

if len(l) == len(r):
    for i in range(len(l)):
        if r[i] != l[i]:
            break

        if r[i] == l[i] and l[i] == '8':
            count += 1

print(count)

# 아래 코드 실패 반례 (1887 1888)
# l, r = input().split()
# count = 0
#
# if len(l) == len(r):
#     for i in range(len(l)):
#         if r[i] == '8' and l[i] == '8':
#             count += 1
#         else:
#             break
#
# print(count)