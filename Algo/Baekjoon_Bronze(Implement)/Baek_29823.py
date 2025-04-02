import sys

n = int(sys.stdin.readline())
direct = sys.stdin.readline().strip()

direction = {
    "N": -1,
    "W": -1,
    "S": 1,
    "E": 1
}

res_horizon = 0
res_vertical = 0

for i in range(len(direct)):
    tmp = direction[direct[i]]
    if direct[i] in ["N", "S"]:
        res_vertical += tmp
    else:
        res_horizon += tmp

print(abs(res_vertical) + abs(res_horizon))

# 다른사람 풀이

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# S = input().rstrip()
# print(abs(S.count('N') - S.count('S')) + abs(S.count('W') - S.count('E')))