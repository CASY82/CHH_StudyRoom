from datetime import datetime, timedelta

while True:
    day, month, year = map(int, input().split())

    if day == 0 and month == 0 and year == 0:
        break

    input_time = datetime(year, month, day)
    first_day = datetime(year, 1, 1)

    if input_time == first_day:
        print(1)
    else:
        diff = input_time - first_day
        print(diff.days + 1)