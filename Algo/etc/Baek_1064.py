# 평행사변형 처리를 할 줄 몰라서 못푼 문제 다른 언어로 된 내용을 참고하여 파이썬으로 나름 변경하였다.

import math
xa, ya, xb, yb, xc, yc = map(int, input().split())
result = []

point_check1 = 1987654321
point_check2 = 1987654321
point_check3 = 1987654321

#세 점이 한 곳에 있는지 확인 하는 법
if xa != xb:
    point_check1 = abs(ya - yb) / abs(xa - xb)
if xb != xc:
    point_check2 = abs(yb - yc) / abs(xb - xc)
if xc != xa:
    point_check3 = abs(yc - ya) / abs(xc - xa)

def line_length(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def square_length(Line1, Line2):
    return (2 * Line1) + (2 * Line2)

if point_check1 == point_check2 == point_check3:
    print('-1')
else:
    L1 = line_length(xa, ya, xb, yb)
    L2 = line_length(xb, yb, xc, yc)
    L3 = line_length(xc, yc, xa, ya)

    result.append(square_length(L1, L2))
    result.append(square_length(L2, L3))
    result.append(square_length(L3, L1))

    print(max(result) - min(result))