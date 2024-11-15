import sys

while True:
    start, diff, finder = map(int, sys.stdin.readline().split())

    if start == diff == finder == 0:
        break

    tmp = finder - start

    if tmp % diff == 0:
        if tmp // diff + 1 <= 0:
            print("X")
        else:
            print(tmp // diff + 1)
    else:
        print("X")

# 다른 사람 풀이
# import sys
# input=sys.stdin.readline
#
# while True :
#     a, b, c = map(int, input().split())
#     if a == b == c == 0 :
#         break
#     if (c - a) % b == 0 and (c - a) // b >= 0 :
#         print((c - a) // b + 1)
#     else : print("X")