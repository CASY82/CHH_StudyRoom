import sys

def format_number(num):
    if isinstance(num, int) or (isinstance(num, float) and num.is_integer()):
        return int(num)
    else:
        return round(num, 4)

a, b, c = map(int, sys.stdin.readline().split())
i, j, k = map(int, sys.stdin.readline().split())

orange = a / i
apple = b / j
pine = c / k

max_juice = min(orange, apple, pine)

print(format_number(a - (max_juice * i)), format_number(b - (max_juice * j)), format_number(c - (max_juice * k)))

# 다른 사람 풀이
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# m = int(1e9)
#
# for i in range(3):
#     m = min(a[i]/b[i], m)
#
# for i in range(3):
#     print(a[i] - b[i]*m, end=' ')