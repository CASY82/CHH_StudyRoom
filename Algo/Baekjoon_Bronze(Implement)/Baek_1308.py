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