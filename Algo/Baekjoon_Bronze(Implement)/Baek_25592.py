import sys

n = int(sys.stdin.readline())

i = 1
result = 0

# 푸앙이는 무조건 홀수
while True:
    if i * (i - 1) // 2 <= n < i * (i + 1) // 2:
        if (i - 1) % 2 == 0:
            print(i * (i + 1) // 2 - n)
        else:
            print(0)
        break
    i += 1

# 다른 사람 풀이

# import sys
# input = sys.stdin.readline
#
# N = int(input())
# i = 1
# turn = 'P'
# while True:
#     if turn == 'P':
#         if N - i <= 0:
#             res = -N+i
#             break
#         turn = 'F'
#     else:
#         if N - i < 0:
#             res = 0
#             break
#         turn = 'P'
#     N -= i
#     i += 1
# print(res)