# 9966
import sys

except_num = ['2', '3', '4', '5', '7']
rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
res = 0
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

def checker(n):
    tmp = list(str(n))
    trans = []
    for ex in except_num:
        if ex in tmp:
            return False

    for j in range(len(tmp)):
        trans.append(rotate_map[tmp[len(tmp) - j - 1]])

    if "".join(tmp) == "".join(trans):
        return True
    else:
        return False

for i in range(n, m + 1):
    if checker(i):
        res += 1

print(res)