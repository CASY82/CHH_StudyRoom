x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

result_x, result_y = 0, 0

#각 좌표당 2번씩 나오면 됨
if x1 == x2:
    result_x = x3
elif x1 == x3:
    result_x = x2
else:
    result_x = x1

if y1 == y2:
    result_y = y3
elif y1 == y3:
    result_y = y2
else:
    result_y = y1

print(result_x, result_y)

#음... 위 코드는 너무 하드 코딩...
# 다른 풀이
# x_nums = []
# y_nums = []
#
# for _ in range(3):
#     x, y = map(int, input().split())
#     x_nums.append(x)
#     y_nums.append(y)
#
# for i in range(3):
#     if x_nums.count(x_nums[i]) == 1:
#         x4 = x_nums[i]
#     if y_nums.count(y_nums[i]) == 1:
#         y4 = y_nums[i]
# print(x4, y4)