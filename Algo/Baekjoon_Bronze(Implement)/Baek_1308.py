import datetime

year, month, days = map(int, input().split())
d_year, d_month, d_days = map(int, input().split())

date_easy = datetime.datetime(year, month, days)
d_day_easy = datetime.datetime(d_year, d_month, d_days)

result = d_day_easy - date_easy

if result.days >= 365243:
    print('gg')
else:
    print('D-%i' %(result.days))

# 다른 사람 풀이(나의 경우는 datetime을 써서 풀었기 때문에 사용하지 않았다면 어떤식을 구현했나 확인하기 위한 용도)
#
# today = list(map(int, input().split()))
# target = list(map(int, input().split()))
#
# dday = 0
# flag = 0
# month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# # 1000년 넘으면 gg 출력
# if target[0] - today[0] > 1000:
#     dday = -1
# elif target[0] - today[0] == 1000:
#     if target[1] > today[1]:
#         dday = -1
#     elif target[1] == today[1]:
#         if target[2] >= today[2]: dday = -1
#
# if dday == -1:
#     print("gg")
#     exit()
#
# for year in range(today[0], target[0] + 1):
#     # 윤년 플래그 1일 때 윤년
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         flag = 1
#     else:
#         flag = 0
#
#     # 윤년이면 month list의 2월 일자를 29일로 바꿔줌
#     if flag == 1:
#         month[1] = 29
#     elif flag == 0:
#         month[1] = 28
#
#     if today[0] == target[0]:
#         if today[1] == target[1]:
#             dday = dday + target[2] - today[2] + 1
#         elif today[1] < target[1]:
#             dday = dday + month[today[1] - 1] - today[2] + 1
#             for i in range(today[1], target[1] - 1):
#                 dday = dday + month[i]
#             dday = dday + target[2]
#         break
#
#     else:
#         if year == today[0]:
#             dday = dday + month[today[1] - 1] - today[2] + 1
#             for i in range(today[1], 12):
#                 dday = dday + month[i]
#
#         elif year == target[0]:
#             for i in range(0, target[1] - 1):
#                 dday = dday + month[i]
#             dday = dday + target[2]
#
#         else:
#             dday = dday + sum(month)
#
# print("D-", dday - 1, sep='')