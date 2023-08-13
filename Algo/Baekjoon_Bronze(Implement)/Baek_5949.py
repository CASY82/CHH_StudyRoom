import sys

n = sys.stdin.readline().strip()
interval = 3  # 구분할 간격

if len(n) > 3:
    n = n[::-1]
    result = ""

    tmp = len(n) % 3

    for i in range(0, len(n)-tmp, interval):
        result += n[i:i + interval] + ","

    if tmp > 0:
        result += n[i + interval:]

    if result[-1] == ",":
        result = result[:len(result)-1]
    print(result[::-1])
else:
    print(n)

# 다른사람 풀이

# n = input()
# comma = 0
#
# if (len(n) / 3) % 1 == 0:
#     repeat = len(n) // 3 - 1
# else:
#     repeat = len(n) // 3
#
# for i in range(repeat):
#     n = n[:((i + 1) * (-3) - comma)] + ',' + n[((i + 1) * (-3) - comma):]
#     comma += 1
#
# print(n)