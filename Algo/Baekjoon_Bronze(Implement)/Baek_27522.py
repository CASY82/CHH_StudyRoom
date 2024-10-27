from datetime import timedelta
import sys

times = []
score = [10, 8, 6, 5, 4, 3, 2, 1]
red = 0
blue = 0

def to_timedelta(time_str):
    minutes, seconds, milliseconds = map(int, time_str.split(':'))
    return timedelta(minutes=minutes, seconds=seconds, milliseconds=milliseconds)

for _ in range(8):
    time, team = sys.stdin.readline().strip().split()
    times.append((time, team))

# 문자열로 정렬
times.sort(key=lambda x: to_timedelta(x[0]))

# 가장 최근 시간을 timedelta로 변환
first = to_timedelta(times[0][0])

for i in range(8):
    if abs(to_timedelta(times[i][0]) - first).total_seconds() > 10:
        continue
    else:
        if times[i][1] == "R":
            red += score[i]
        else:
            blue += score[i]

if red > blue:
    print("Red")
else:
    print("Blue")
