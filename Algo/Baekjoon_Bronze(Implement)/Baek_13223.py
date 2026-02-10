# 소금 폭탄
import sys

time1 = sys.stdin.readline().strip()
time2 = sys.stdin.readline().strip()

format_str = "%H:%M:%S"

def time_to_seconds(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

sec1 = time_to_seconds(time1)
sec2 = time_to_seconds(time2)

if sec2 <= sec1:
    sec2 += 86400

diff = sec2 - sec1

print(seconds_to_time(diff))