# 조건을 잘못찾음...

# x, y, w, s = map(int, input().split())
#
# result = 0
#
# if (w * 2) > s:
#     이 부분을 한참 헤맴... 결국 못품. x와 y를 비교할게 아니었다는 것을 깨달음
#     if x < y:
#         result = (y - x) * w + x * s
#     else:
#         result = (x - y) * w + y * s
# else:
#     result = (x + y) * w
#
# print(result)

X, Y, W, S = map(int, input().split())
X, Y = min(X, Y), max(X, Y)
if S < W*2:
    s, b = min(X, Y), max(X, Y)
    if S <= W:
        #x+y가 짝수일 때는 딱 맞아 떨어짐. 즉 대각선 이동만 생각하는 경우
        m = (X+Y)%2
        print((Y-m)*S + m*W)
    else:
        #대각선 이동 + 평행이동이 섞인 경우
        print(X*S + (Y-X)*W)
else:
    #평행이동만 하는게 빠른 경우
    print((X+Y)*W)
