import sys
import datetime

n = int(sys.stdin.readline())

def cal_date(n):
    start_date = datetime.date(2014, 4, 2)
    cal_days = datetime.timedelta(days=n - 1)
    return (start_date + cal_days).strftime('%Y-%m-%d')

res = cal_date(n)
print(res)