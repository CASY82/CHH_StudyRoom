import sys

def my_round(num, ndigits=0):
    if ndigits >= 0:
        multiplier = 10 ** ndigits
        return int(num * multiplier + 0.5) / multiplier
    else:
        multiplier = 10 ** abs(ndigits)
        return int(num / multiplier + 0.5) * multiplier

n = int(sys.stdin.readline())

score = []

if n != 0:
    for _ in range(n):
        score.append(int(sys.stdin.readline()))

    score.sort()
    trimmed_mean = my_round(n * 0.15, 0)
    trimmed_mean = int(trimmed_mean)

    tmp = score[trimmed_mean:len(score) - trimmed_mean]

    print(int(my_round(sum(tmp) / len(tmp), 0)))
else:
    print(0)

# 다른 사람 풀이

# from collections import deque
# import io, os, sys
#
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#
#
# def custom_round(num):
#     if int(num) * 2 < int(num * 2):
#         return int(num) + 1
#     else:
#         return int(num)
#
#
# n = int(input())
# li = [int(input()) for _ in range(n)]
# li.sort()
#
# if not li:
#     print(0)
# else:
#     affected = custom_round(n / 100 * 15)
#
#     deq = deque(li)
#     for _ in range(affected):
#         deq.popleft()
#         deq.pop()
#
#     avg = sum(deq) / len(deq)
#
#     result = custom_round(avg)
#
#     print(result)