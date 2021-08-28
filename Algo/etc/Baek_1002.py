# 원이 만나는지 안만나는지 확인하는 방법은 다음과 같다.(두 점이 서로의 원 밖에 있을 때)
# 1. 두 점 사이의 거리를 구한다.
# 2. 사전에 주어진 두 거리를 더한 합보다 두 점 사이거리가 작으면 두 원은 겹친다. ==> 2개
# 3. 사전에 주어진 두 거리를 더한 합과 두 점 사이의 거리가 동일하면 두 원은 접한다. ==> 1개
# 4. 사전에 주어진 두 거리를 더한 합보다 두 점 사이의 거리가 크면 두 원은 만나지 않는다. ==> 0개
# 5. 두 점과 거리가 겹친다 ==> 무한
# 반대로 큰 원 안에 작은 원이 들어가 있는 경우 다음과 같이 구한다.
# 1. 일단 두 점 사이의 거리가 큰 원의 반지름보다 작은 경우 다음 로직을 통하게 한다.
# 2. 두 점 사이의 거리와 작은 원의 반지름을 더한 결과가 큰 원의 반지름보다 크다. ==> 2개
# 3. 두 점 사이의 거리와 작은 원의 반지름을 더한 결과가 큰 원의 반지름과 같다. ==> 1개
# 4. 두 점 사이의 거리와 작은 원의 반지름을 더한 결과가 큰 원의 반지름보다 작다. ==> 0개
# 한번에 성공!

import math

t = int(input())
xylen_list = []

for i in range(t):
    xylen_list.append(list(map(int, input().split())))

def two_point_len(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))


for i in range(len(xylen_list)):
    if xylen_list[i][2] > xylen_list[i][5]:
        big_circle_half = xylen_list[i][2]
        small_circle_half = xylen_list[i][5]
    else:
        big_circle_half = xylen_list[i][5]
        small_circle_half = xylen_list[i][2]


    if xylen_list[i][0] == xylen_list[i][3] and xylen_list[i][1] == xylen_list[i][4] and xylen_list[i][2] == xylen_list[i][5]:
        print('-1')
    else:
        if two_point_len(xylen_list[i][0], xylen_list[i][1], xylen_list[i][3], xylen_list[i][4]) < big_circle_half:
            if two_point_len(xylen_list[i][0], xylen_list[i][1], xylen_list[i][3], xylen_list[i][4]) + small_circle_half > big_circle_half:
                print('2')
            elif two_point_len(xylen_list[i][0], xylen_list[i][1], xylen_list[i][3], xylen_list[i][4]) + small_circle_half == big_circle_half:
                print('1')
            else:
                print('0')
        else:
            if two_point_len(xylen_list[i][0], xylen_list[i][1], xylen_list[i][3], xylen_list[i][4]) > big_circle_half + small_circle_half:
                print('0')
            elif two_point_len(xylen_list[i][0], xylen_list[i][1], xylen_list[i][3], xylen_list[i][4]) == big_circle_half + small_circle_half:
                print('1')
            else:
                print('2')

#좀 더 깔끔한 정답이 있어서 첨부한다.
# import math
#
# n = int(input())
#
# for i in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int,input().split())
#     distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
#     if distance == 0 and r1==r2:
#         print(-1)
#     elif abs(r1-r2)==distance or r1+r2 == distance:
#         print(1)
#     elif abs(r1-r2)<distance<r1+r2:
#         print(2)
#     else: print(0)