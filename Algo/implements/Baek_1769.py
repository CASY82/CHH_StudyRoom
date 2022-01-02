#문제 이해를 잘못함 범위가 100만까지인줄 알았는데, 자리수가 100만 자리 즉 10^100까지 범위였다.
#아래코드는 시간 초과
# import sys
#
# x = int(sys.stdin.readline())
# tmp = x
# check = False
# cnt = 0
#
# while True:
#     result = 0
#     while tmp > 0:
#         result += tmp % 10
#         tmp //= 10
#
#     tmp = result
#     cnt += 1
#
#     if result % 3 == 0:
#         check = True
#         break
#
#     if result < 10:
#         break
#
# if check:
#     print(cnt)
#     print("YES")
# else:
#     print(cnt)
#     print("NO")

import sys

x = list(map(int, sys.stdin.readline().strip()))
check = False
cnt = 0

if len(x) < 2:
    tmp = sum(x)

    if tmp % 3 == 0:
        check = True

else:
    while True:
        tmp = sum(x)
        x = list(map(int, str(tmp)))
        cnt += 1

        #여기서 break를 걸면 어떻게하니... 멍청아... 문제이해를 못했네
        if tmp % 3 == 0:
            check = True

        if len(x) < 2:
            break

if check:
    print(cnt)
    print("YES")
else:
    print(cnt)
    print("NO")