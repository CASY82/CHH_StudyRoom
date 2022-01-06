# import sys
#
# n = int(sys.stdin.readline())
# cnt = 0
#
# # 일단 브루트 포스 아마 시간 초과가 날거다
# for i in range(1000001):
#     tmp = i
#     check = True
#     while True:
#         if len(str(tmp)) <= 1:
#             break
#
#         new_tmp = tmp % 10
#
#         if tmp // 10 % 10 > new_tmp:
#             check = True
#         else:
#             check = False
#             break
#
#         tmp //= 10
#
#     if check:
#         print(i)
#         cnt += 1
#
#     if n == cnt:
#         break
#
#     if cnt == 847:
#         i = -1
#         break
#
# print(i)

# import sys
# sys.setrecursionlimit(10 ** 5)
#
# n = int(sys.stdin.readline())
# numList = [str(i) for i in range(9, -1, -1)]
#
# locate = []
# tmp = []
#
# #맞게 구현은 했는데 거꾸로 됨;;
# def backtrack(startlen, endlen, num):
#     if startlen == endlen:
#         for i in range(len(locate)):
#             tmp.append(int(''.join(locate)))
#
#     else:
#         #집어 넣을 숫자
#         for j in range(num, len(numList)):
#             locate.append(numList[j])
#             backtrack(startlen+1, endlen, j+1)
#             locate.pop()
#
# # 숫자의 자릿수X 문제 이해 실패...
# for i in range(7):
#     backtrack(0, i, 0)
#
# tmp = list(set(tmp))
# tmp.sort()
#
# print(tmp)
# print(len(tmp))
#
# if n <= len(tmp):
#     print(tmp[n-1])
# else:
#     print(-1)

#
# import sys
#
# n = int(sys.stdin.readline())
# numList = [i for i in range(10)]
#
# locate = []
# cnt = [0]
#
# def backtrack(startlen, endlen, num):
#     if startlen > endlen:
#         for i in range(len(locate)):
#             print(locate[i], end=' ')
#         print()
#         cnt[0] += 1
#
#     else:
#         #집어 넣을 숫자
#         for j in range(len(numList)):
#             locate.append(numList[j])
#             backtrack(startlen+1, endlen, j)
#             locate.pop()
#
# # 숫자의 자릿수
# for i in range(7):
#     backtrack(0, i, 0)
#
# print(cnt[0])

import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())
numList = [str(i) for i in range(9, -1, -1)]

locate = []
tmp = []

#맞게 구현은 했는데 거꾸로 됨;;
def backtrack(startlen, endlen, num):
    if startlen == endlen:
        for i in range(len(locate)):
            if not int(''.join(locate)) in tmp:
                tmp.append(int(''.join(locate)))

    else:
        #집어 넣을 숫자
        for j in range(num, len(numList)):
            locate.append(numList[j])
            backtrack(startlen+1, endlen, j+1)
            locate.pop()

for i in range(11):
    backtrack(0, i, 0)

tmp.sort()

if n <= len(tmp):
    print(tmp[n-1])
else:
    print(-1)