r, c, n = map(int, input().split())

if r % n == 0 and c % n == 0:
    print((r // n) * (c // n))
else:
    if r % n != 0 and c % n == 0:
        print(((r // n) + 1) * (c // n))
    elif c % n != 0 and r % n == 0:
        print((r // n) * ((c // n) + 1))
    else:
        print(((r // n) + 1) * ((c // n) + 1))

#참고한 소스;; 그냥 반올림하는 문제였다...
# a, b, c = map(int, input().split())
# import math
# print(math.ceil(a/c) * math.ceil(b/c))