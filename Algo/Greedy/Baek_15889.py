# 호 안에 수류탄이야!!
import sys

n = int(sys.stdin.readline())
location = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print("권병장님, 중대장님이 찾으십니다")
    sys.exit(0)

intersection = list(map(int, sys.stdin.readline().split()))

res = True
max_range = 0

for i in range(n - 1):
    if location[i] > max_range:
        res = False
        break
    else:
        max_range = max(max_range, location[i] + intersection[i])

if max_range < location[-1]:
    res = False

if res:
    print("권병장님, 중대장님이 찾으십니다")
else:
    print("엄마 나 전역 늦어질 것 같아")