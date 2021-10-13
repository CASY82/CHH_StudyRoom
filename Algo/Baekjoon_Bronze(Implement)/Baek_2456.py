n = int(input())
hubo = [0 for i in range(3)]
point = [[0 for i in range(3)] for j in range(3)]
same_prize = False

for _ in range(n):
    one, two, three = map(int, input().split())

    hubo[0] += one
    hubo[1] += two
    hubo[2] += three

    for j in range(1, 4):
        if one == j:
            point[0][j-1] += 1

        if two == j:
            point[1][j-1] += 1

        if three == j:
            point[2][j-1] += 1

counter = 0
final = True

for i in range(3):
    if max(hubo) == hubo[i]:
        counter += 1

if counter >= 2:
    same_prize = True

if (same_prize == True):
    winner = []
    kaijou = 0
    for k in range(3):
        if max(point[0][2], point[1][2], point[2][2]) == point[k][2]:
            winner.append(k)
            kaijou = k

    if len(winner) == 2:
        sec_winner = []
        for k in winner:
            if max(point[winner[0]][1], point[winner[1]][1]) == point[k][1]:
                sec_winner.append(k)
                kaijou = k

        if len(sec_winner) == 2:
            th_winner = []
            for k in sec_winner:
                if max(point[sec_winner[0]][0], point[sec_winner[1]][0]) == point[k][0]:
                    th_winner.append(k)
                    kaijou = k
        elif len(sec_winner) == 3:
            th_winner = []
            for k in sec_winner:
                if max(point[0][0], point[1][0], point[2][0]) == point[k][0]:
                    th_winner.append(k)
                    kaijou = k

        if len(th_winner) >= 2:
            print(0, max(hubo))
            final = False

    elif len(winner) == 3:
        sec_winner = []
        for k in winner:
            if max(point[0][1], point[1][1], point[2][1]) == point[k][1]:
                sec_winner.append(k)
                kaijou = k

        if len(sec_winner) == 2:
            th_winner = []
            for k in sec_winner:
                if max(point[sec_winner[0]][0], point[sec_winner[1]][0]) == point[k][0]:
                    th_winner.append(k)
                    kaijou = k
        elif len(sec_winner) == 3:
            th_winner = []
            for k in sec_winner:
                if max(point[0][0], point[1][0], point[2][0]) == point[k][0]:
                    th_winner.append(k)
                    kaijou = k

        if len(th_winner) >= 2:
            print(0, max(hubo))
            final = False

    if final:
        print(kaijou + 1, hubo[kaijou])

elif (same_prize == False):
    print(hubo.index(max(hubo)) + 1, max(hubo))

'''
6
1 2 3
1 2 3
1 3 2
1 3 2
3 1 2
3 2 1

출력
0 13


4
1 2 3
2 1 3
3 2 1
2 3 1

출력
3 8

4
3 1 2
1 3 2
2 3 1
3 2 1

출력
0 9
'''

#똑똑한 풀이 참고
#
# n = int(input())
#
# arr1 = [0] * 3
# arr2 = [0] * 3
#
# for i in range(n):
#     x, y, z = map(int, input().split())
#     arr1[0] += x
#     arr1[1] += y
#     arr1[2] += z
#
#     arr2[0] += x * x
#     arr2[1] += y * y
#     arr2[2] += z * z
#
# m = max(arr1)
#
# if arr1.count(m) == 1:
#     for i in range(len(arr1)):
#         if arr1[i] == m:
#             print(i + 1, m)
#             break
# else:
#     power = max(arr2)
#     idx = 0
#     for i in range(len(arr2)):
#         if arr2[i] == power:
#             idx = i
#             break
#
#     if arr2.count(power) > 1:
#         print(0, arr1[idx])
#     else:
#         print(idx + 1, arr1[idx])