# 와우산 스탬프 투어
import sys

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())

res = 0
# 방문한 명소당 10점
res += n * 10

# 방문한 명소 3 이상 추가 점수
if n >= 3:
    res += 20

# 모든 명소 방문 특별 점수 50
if n == 5:
    res += 50

# 1000보 초과 -15
if w > 1000:
    if res - 15 < 0:
        res = 0
    else:
        res -= 15

print(res)