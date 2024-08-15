import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    fir_check = ""
    cnt = 0

    blue = list(map(int, sys.stdin.readline().split()))
    red = list(map(int, sys.stdin.readline().split()))

    blue_loc = 0
    red_loc = 0

    for i in range(n):
        blue_loc += blue[i]
        red_loc += red[i]

        if fir_check == "":
            if blue_loc > red_loc:
                fir_check = "blue"
            elif blue_loc < red_loc:
                fir_check = "red"
        else:
            if fir_check == "red" and blue_loc > red_loc:
                cnt += 1
                fir_check = "blue"
            elif fir_check == "blue" and blue_loc < red_loc:
                cnt += 1
                fir_check = "red"

    print(cnt)

# 다른 사람 풀이
# import sys
# def input():return sys.stdin.readline().rstrip()
# while (n:=int(input())):
#     lstx = list(map(int, input().split()))
#     lsty = list(map(int, input().split()))
#     if lstx[0] > lsty[0]:
#         x = 1
#     elif lstx[0] < lsty[0]:
#         x = -1
#     else:
#         x = 0
#     a = lstx[0]
#     b = lsty[0]
#     cnt = 0
#     for i in range(1, n):
#         a += lstx[i]
#         b += lsty[i]
#         if a > b:
#             y = 1
#         elif a < b:
#             y = -1
#         else:
#             y = 0
#         if x and y and x*y == -1:
#             cnt += 1
#             x = y
#         elif not x:
#             x = y
#     print(cnt)