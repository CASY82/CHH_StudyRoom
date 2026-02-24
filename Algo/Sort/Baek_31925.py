# APC2shake!
import sys

n = int(sys.stdin.readline())

res = []
tmp = []

# 아주대 재학생(school) : jaehak
# 경시대회 수상자가 아닌자(icpc) : notyet
# shake! 3위 이내가 아닌자 : shake_top > 3 or shake_top == -1
# 위 규칙 만족하는 사람 중 apc_score <= 10

for _ in range(n):
    name, school, icpc, shake_top, apc_score = sys.stdin.readline().strip().split()

    shake_top = int(shake_top)
    apc_score = int(apc_score)

    if school == "jaehak" and icpc == "notyet" and (shake_top > 3 or shake_top == -1):
        tmp.append([name, apc_score])

tmp.sort(key=lambda x: x[1])

for i in range(min(10, len(tmp))):
    res.append(tmp[i][0])

res.sort()

print(len(res))
for n in res:
    print(n)