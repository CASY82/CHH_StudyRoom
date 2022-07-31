import sys

#내 정답은 집합으로 푼거
while True:
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    sang_cd = set()
    sun_cd = set()

    for _ in range(n):
        sang_cd.add(int(sys.stdin.readline()))

    for _ in range(m):
        sun_cd.add(int(sys.stdin.readline()))

    print(len(sang_cd & sun_cd))

#아마도 이분탐색으로 푼 풀이 인듯?
# import sys; input = sys.stdin.readline
# while True:
#     N, M = map(int, input().split())
#     if N == M == 0:
#         break
#     A = [int(input()) for _ in range(N)]
#     B = [int(input()) for _ in range(M)]
#     if not N or not M:
#         print(0)
#         continue
#     n = m = answer = 0
#     while True:
#         if A[n] == B[m]:
#             answer += 1
#             if m == M - 1:
#                 if n == N - 1:
#                     break
#                 n += 1
#             else:
#                 n += 1
#                 m += 1
#         else:
#             if A[n] < B[m] or m == M - 1:
#                 if n == N - 1:
#                     break
#                 n += 1
#             else:
#                 m += 1
#     print(answer)