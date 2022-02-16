import datetime
import sys

d, m = map(int, sys.stdin.readline().split())
result = datetime.datetime(2009, m, d).weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[result])