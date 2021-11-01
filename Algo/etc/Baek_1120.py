# a, b = input().split()
# diff = 0
#
# if len(a) != len(b):
#     diff = abs(len(b) - len(a))
#
# tmp_front = a
# tmp_back = a
# front_count = 0
# back_count = 0
#
# for i in range(diff-1, -1, -1):
#     tmp_front = b[i] + tmp_front
#     tmp_back = tmp_back + b[len(b) - 1 - i]
#
# print(tmp_front, tmp_back)
#
# for j in range(len(b)):
#     if tmp_front[j] != b[j]:
#         front_count += 1
#
#     if tmp_back[j] != b[j]:
#         back_count += 1
#
# print(front_count, back_count)
# print(min(front_count, back_count))

a, b = input().split()
result = []

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if a[j] == b[j + i]:
            count += 1

        if j == len(a) - 1:
            result.append(count)

print(len(a) - max(result))