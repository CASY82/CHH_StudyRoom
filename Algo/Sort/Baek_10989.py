#메모리 초과. 카운팅 정렬을 이용하여 푸는 문제다.
# import sys
# n = int(sys.stdin.readline())
# num = []
#
# for _ in range(n):
#     num.append(int(sys.stdin.readline()))
#
# num.sort()
#
# for i in num:
#     print(i)

import sys
n = int(sys.stdin.readline())
num = [0] * 10001

for _ in range(n):
    in_num = int(sys.stdin.readline())

    num[in_num] += 1

for i in range(len(num)):
    for j in range(num[i]):
        print(i)