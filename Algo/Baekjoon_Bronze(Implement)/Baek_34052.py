# 체육은 수학과목 입니다 2
import sys

data = []

for _ in range(4):
    data.append(int(sys.stdin.readline()))

if sum(data) + 300 <= 1800:
    print("Yes")
else:
    print("No")