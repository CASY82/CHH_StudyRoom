import sys

n = int(sys.stdin.readline())

for case in range(1, n + 1):
    c = int(sys.stdin.readline())
    i = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    tmp = []
    check = False

    for fir in range(len(p)):
        for sec in range(fir):
            if p[fir] + p[sec] == c:
                tmp.append(fir + 1)
                tmp.append(sec + 1)
                check = True
                break
        if check:
            break

    tmp.sort()
    print("Case #{0}: {1} {2}".format(case, tmp[0], tmp[1]))

# 다른 사람 코드
# import sys; input = sys.stdin.readline
#
# def solve():
#     C = int(input())
#     I = int(input())
#     P = list(map(int, input().split()))
#     for i in range(I - 1):
#         for j in range(i + 1, I):
#             if P[i] + P[j] == C:
#                 print(i + 1, j + 1)
#                 return
#
# for i in range(1, int(input()) + 1):
#     print('Case #%d: ' % i, end = '')
#     solve()