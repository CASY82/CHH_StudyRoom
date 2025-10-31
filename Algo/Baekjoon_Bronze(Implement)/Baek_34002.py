import sys

a, b, c = map(int, sys.stdin.readline().split())
s, v = map(int, sys.stdin.readline().split())
l = int(sys.stdin.readline())

total_exp = (250 - l) * 100
time = 0
phases = [
    (v * 30, c),  # VIP 사우나
    (s * 30, b),  # 심신 수련관
    (10 ** 18, a),  # 이벤트 맵(무한)
]
for minutes, rate in phases:
    if total_exp <= 0:
        break
    # 이 구간만 쓴다면 필요한 분
    need_minutes = (total_exp + rate - 1) // rate
    use = min(minutes, need_minutes)
    time += use
    total_exp -= use * rate

print(time)