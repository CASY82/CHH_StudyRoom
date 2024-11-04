import sys

t = int(sys.stdin.readline())

for _ in range(t):
    fir, sec, third = map(int, sys.stdin.readline().split())

    print(fir, sec, third)
    if max(fir, sec, third) < 10:
        print("zilch")
    elif min(fir, sec, third) >= 10:
        print("triple-double")
    elif (fir < 10 and min(sec, third) >= 10) or (sec < 10 and min(fir, third) >= 10) or (third < 10 and min(fir, sec) >= 10):
        print("double-double")
    elif (fir >= 10 and max(sec, third) < 10) or (sec >= 10 and max(fir, third) < 10) or (third >= 10 and max(sec, fir) < 10):
        print("double")

    print()

# 다른 사람 풀이
# t = int(input())
# for _ in range(t):
#     a, b, c = map(int, input().split())
#     cnt = 0
#     for i in [a, b, c]:
#         if i >= 10:
#             cnt += 1
#     print(a, b, c)
#     if cnt == 0:
#         print('zilch')
#     elif cnt == 1:
#         print('double')
#     elif cnt == 2:
#         print('double-double')
#     else:
#         print('triple-double')
#     print()