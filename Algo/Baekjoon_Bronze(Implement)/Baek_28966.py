# Доктор Стрэндж и перестановка
# import sys
#
# n = int(sys.stdin.readline())
# nums = list(map(int, sys.stdin.readline().split()))
#
# tmp = []
#
# for i in range(n):
#     if nums[i] % 2 != (i + 1) % 2:
#         tmp.append(i + 1)
#
# if len(tmp) == 0:
#     if n >= 3:
#         print(1, 3)
#     else:
#         print(-1, -1)
# elif len(tmp) == 2:
#     print(tmp[0], tmp[1])
# else:
#     print(-1, -1)

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

bad = []
for i in range(n):
    if (a[i] % 2) != ((i + 1) % 2):
        bad.append(i)

def ok(arr):
    for i in range(n):
        if (arr[i] % 2) != ((i + 1) % 2):
            return False
    return True

if len(bad) == 0:
    # 이미 조건 만족. "반드시 1번 swap" 해야 하므로
    # swap 후에도 조건이 유지되는 쌍을 찾아야 함.
    # 같은 parity 위치끼리 바꾸면 유지됨(홀수<->홀수 or 짝수<->짝수).
    if n >= 3:
        print(1, 3)
    else:
        # n==2면 서로 다른 두 칸(1,2)만 swap 가능한데 홀<->짝 교환이라 조건 깨짐
        print(-1, -1)

elif len(bad) == 2:
    i, j = bad[0], bad[1]
    b = a[:]
    b[i], b[j] = b[j], b[i]
    if ok(b):
        print(i + 1, j + 1)
    else:
        print(-1, -1)
else:
    print(-1, -1)
