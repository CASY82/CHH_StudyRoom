# Snowman

import sys

snow = sys.stdin.readline().strip()
n = int(sys.stdin.readline())

# 일단 제일 작은 문자가 맨앞에 와야 하니 제일 작은 문자가 먼저 선택
# 그 다음 양 옆을 색인했을때, 작은 문자 택
# 반복

start = min(snow)
res = start
tmp = []

for i in range(len(snow)):
    if snow[i] == start:
        if i == 0:
            tmp.append(snow[i + 1])
        elif i == len(snow) - 1:
            tmp.append(snow[i - 1])
        else:
            tmp.append(snow[i + 1])
            tmp.append(snow[i - 1])

res_array = [min(tmp), start]

for i in range(n - 1):
    res = res + res_array[i % 2]

print(res)

