import sys

s = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

cost = 250
diff = s - a

if diff % b != 0:
    tmp = diff // b + 1
else:
    tmp = diff // b

if s > a:
    print(cost + (tmp * 100))
else:
    print(250)

# 다른 사람 풀이

# import math
#
# S=int(input())
# A=int(input())
# B=int(input())
#
# pay=250
# if S>A:
#     height=S-A
#     pay += math.ceil(height/B)*100
# print(pay)