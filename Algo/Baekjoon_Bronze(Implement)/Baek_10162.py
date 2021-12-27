import sys

t = int(sys.stdin.readline())

a = 300
b = 60
c = 10
result = [0] * 3

if t % c != 0:
    print(-1)
else:
    while t > 0:
        if t // a > 0:
            result[0] = t // a
            t %= a

        if t // b > 0:
            result[1] = t // b
            t %= b

        if t // c > 0:
            result[2] = t // c
            t %= c

    print(result[0], result[1], result[2])

# 좀 더 줄일 수 있었으나 안정적으로 위 코드와 같이 짜봤다. 아래는 참고
# t = int(input())
#
# if t // 300 == 0 and t%10 == 0:
#
#     print(t//300, t//60, (t%60)//10)
# elif t// 300 != 0 and t%10 == 0:
#     y=(t%300)
#     print(t//300, y//60, (y%60)//10)
# else :
#     print(-1)