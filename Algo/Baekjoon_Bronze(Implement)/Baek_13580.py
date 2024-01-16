import sys

a, b, c = map(int, sys.stdin.readline().split())
result = False
tmp = [a, b, c]
tmp.sort()

# 두번만에 돌아오는 경우
if abs(a - b) == 0 or abs(c - b) == 0 or abs(a - c) == 0:
    result = True
# 세번만에 돌아오는 경우
elif tmp[2] == tmp[1] + tmp[0]:
    result = True

if result:
    print("S")
else:
    print("N")