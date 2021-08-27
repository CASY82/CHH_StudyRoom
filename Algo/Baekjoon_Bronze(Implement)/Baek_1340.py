# 실패가 자꾸 뜬다. 하나하나 구현하는 방법으로 다시시도

# import datetime
#
# month, day, year, time_in = input().split()
# mon = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#
# day = int(day[0:2])
# hour = int(time_in[0:2])
# min = int(time_in[3:5])
#
# date_input = datetime.datetime(int(year), mon.index(month), day, hour, min)
# new_year = datetime.datetime(int(year) + 1, 1, 1, 0, 0)
# old_year = datetime.datetime(int(year), 1, 1, 0, 0)
#
# old_min = ((date_input - old_year).days) * 1440 + min
# whole_min = ((new_year - old_year).days) * 1440
#
#
# print((100 * old_min / whole_min))
#






month, day, year, time_in = input().split()
mon = ['none', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = int(day[0:2])
hour = int(time_in[0:2])
min = int(time_in[3:5])
year = int(year)
days = 0
whole_times = 0

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    whole_times = 366 * 24 * 60
    for i in range(mon.index(month) - 1):
        days += mon_day[i]


    if mon.index(month) > 2:
        days += 1

    now_times = (days + day - 1) * 24 * 60 + hour * 60 + min

else:
    whole_times = 365 * 24 * 60
    for i in range(mon.index(month) - 1):
        days += mon_day[i]

    now_times = (days + day - 1) * 24 * 60 + hour * 60 + min

print(100 * now_times / whole_times)













# 다른사람풀이 참고
# Month, D, Y, T = input().split()
# D = int(D[:-1])
# Y = int(Y)
# H, M = map(int, T.split(':'))
# month_name_li = ["January" , "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"]
# month_day_li = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if Y%400 == 0 or (Y%4 == 0 and Y%100 != 0):
#     month_day_li[1] += 1
# total_time = sum(month_day_li) * 24 * 60
#
# last_month_idx = month_name_li.index(Month)
# current_time = (sum(month_day_li[:last_month_idx]) + D-1)*24*60 + H*60 + M
# print(current_time/total_time * 100)
# print(current_time) # 185791
# print(total_time)# 525600