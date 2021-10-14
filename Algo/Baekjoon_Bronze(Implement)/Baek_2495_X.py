# for _ in range(3):
#     num_count = [0 for i in range(10)]
#     num = input()
#
#     for i in range(1, len(num)):
#         if num[i] == num[i - 1]:
#             num_count[int(num[i])] += 1
#
#     if max(num_count) == 0:
#         print(1)
#     else:
#         print(num_count[num_count.index(max(num_count))] + 1)

# 반례를 못찾음
# for _ in range(3):
#     num_count = [0 for i in range(10)]
#     num = input()
#     i = 0
#
#     while i < 8:
#         count = 0
#         for j in range(i + 1, len(num)):
#             if num[i] == num[j]:
#                 count += 1
#
#             if num[i] != num[j] or j == 7:
#                 i = j
#                 break
#
#         num_count[int(num[i])] = count
#
#         if i == 7:
#             i += 1
#
#     if max(num_count) == 0:
#         print(1)
#     else:
#         print(max(num_count) + 1)

def cnt(s):
    count = 1
    max_count = 1
    compare = s[0]

    for n in s[1:]:
        if n == compare:
            count += 1
        else:
            max_count = max(max_count, count)
            compare = n
            count = 1

    max_count = max(max_count, count)
    return max_count

for _ in range(3):
    print(cnt(input()))
