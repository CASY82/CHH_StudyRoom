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

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# h1, m1, s1 = map(int, input().split(':'))
# h2, m2, s2 = map(int, input().split(':'))
# t1 = h1*60*60 + m1*60 + s1
# t2 = h2*60*60 + m2*60 + s2
# t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
# h = t//60//60
# m = t//60 % 60
# s = t%60
# print("%02d:%02d:%02d" % (h, m, s))