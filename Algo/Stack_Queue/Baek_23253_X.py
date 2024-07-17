# 반례 못찾음
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
#
# stack = []
# last = 0
# res = True
#
# for i in range(m):
#     book = int(sys.stdin.readline())
#
#     stack.append(list(map(int, sys.stdin.readline().split())))
#
# index = 0
#
# while True:
#     if stack[index % m][-1] == last + 1:
#         last += 1
#         stack[index % m].pop()
#     else:
#         if m - 1 == index % m:
#             res = False
#             break
#
#     if last == n:
#         break
#
#     index += 1
#
# if res:
#     print("Yes")
# else:
#     print("No")

import sys

n, m = map(int, sys.stdin.readline().split())
books = []
for _ in range(m):
    k = int(sys.stdin.readline())
    book = list(map(int, sys.stdin.readline().split()))
    if book == sorted(book, reverse=True):
        books.append(book)
    else:
        print("No")
        exit()
print("Yes")

# 다른 사람 풀이
# # 빠른 입력
# import sys
# def input(): return sys.stdin.readline().rstrip()
# from collections import deque
#
# # 입력부
# N, M = map(int, input().split())
#
# # 책 정렬 여부 확인
# result = 'Yes'
# for i in range(M):
#     k = int(input())
#     stack = deque(list(map(int, input().split())))
#
#     # 스택에서 값을 빼가며 정렬 여부 확인
#     last_value = 0
#     while stack:
#         value = stack.pop()
#         if value < last_value:
#             result = 'No'
#             break
#         last_value = value
#
#     if result == 'No': break
#
# # 출력부
# print(result)