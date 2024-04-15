import sys

first_time = list(map(int, sys.stdin.readline().split(":")))
second_time = list(map(int, sys.stdin.readline().split(":")))

first_total_seconds = first_time[0] * 3600 + first_time[1] * 60 + first_time[2]
second_time_total_seconds = second_time[0] * 3600 + second_time[1] * 60 + second_time[2]

if first_total_seconds - second_time_total_seconds > 0:
    result_time = 24 * 3600 - (first_total_seconds - second_time_total_seconds)
elif first_total_seconds - second_time_total_seconds < 0:
    result_time = abs(first_total_seconds - second_time_total_seconds)
else:
    result_time = 24 * 3600

hour = result_time // 3600
minute = (result_time % 3600) // 60
seconds = (result_time % 3600) % 60

print(f"{hour:02d}:{minute:02d}:{seconds:02d}")