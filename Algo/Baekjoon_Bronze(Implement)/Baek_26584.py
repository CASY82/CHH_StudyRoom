import sys

n = int(sys.stdin.readline())

year_static = 60 * 24 * 365
day_static = 60 * 24
hour_static = 60

for _ in range(n):
    title, time = sys.stdin.readline().strip().split(",")

    time = int(time)

    year = time // year_static
    time %= year_static
    day = time // day_static
    time %= day_static
    hour = time // hour_static
    time %= hour_static

    result = title + " - "

    if year != 0:
        result += str(year) + " year(s) "

    if day != 0:
        result += str(day) + " day(s) "

    if hour != 0:
        result += str(hour) + " hour(s) "

    result += str(time) + " minute(s)"

    print(result)