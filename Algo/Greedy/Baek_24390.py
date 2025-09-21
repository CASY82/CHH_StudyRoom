import sys

def mmss_to_seconds(time_str: str) -> int:
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

times = sys.stdin.readline().strip()

res = 0
tmp = mmss_to_seconds(times)
start = True

selectors = [600, 60, 30, 10]

for button in selectors:
    while tmp >= button:
        tmp -= button
        res += 1
        if button == 30:
            start = False

if start:
    res += 1
print(res)