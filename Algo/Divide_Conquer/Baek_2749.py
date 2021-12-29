#앞에서 피사노를 연습한 보람이 있었다.... 성공!
import sys

n = int(sys.stdin.readline())

mem = [0, 1] + [0] * (15 * (10 ** 5))
PISANO = 1000000

i = 2
while i < len(mem):
    mem[i] = (mem[i-1] + mem[i-2]) % PISANO

    i += 1

#아 여기서 나머지 연산 하는 수를 자꾸 실수해서 4번이나 틀리다니;;;;
print(mem[n%(len(mem)-2)])

# dp와 딕셔너리를 이용한 풀이 되시겠다.. n//2 를 한 이유를 사실 잘 모르겠다
#
# dp = dict()
#
# def fibo(n):
#       if dp.get(n) != None:
#             return dp[n]
#       if n == 0:
#             return 0
#       if n == 1 or n == 2:
#             return 1
#       if n % 2 == 0:
#             dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000
#             dp[n // 2 - 1] = fibo(n // 2 - 1) % 1000000
#             return dp[n // 2 + 1] ** 2 - dp[n // 2 - 1] ** 2
#       else:
#             dp[n // 2 + 1] = fibo(n // 2 + 1) % 1000000
#             dp[n // 2] = fibo(n // 2) % 1000000
#             return dp[n // 2 + 1] ** 2 + dp[n // 2] ** 2
#
# print(fibo(int(input())) % 1000000)

# 이 풀이도 왜 풀리는지 모르겠지만 나중에 다시 뭘 이용했는지 확인해볼 필요는 있겠다.

# import sys
#
# input = sys.stdin.readline
#
# N = int(input())
#
# A = [[1, 1], [1, 0]]
# u = [[1], [0]]
#
#
# def mtx_mul(alist, blist, a, b):
#     mtx = [[0 for _ in range(b)] for _ in range(a)]
#
#     for _ in range(a):
#         for i in range(b):
#             for j in range(a):
#                 mtx[_][i] += alist[_][j] * blist[j][i]
#
#     for _ in range(a):
#         for i in range(b):
#             mtx[_][i] %= 1000000
#
#     return mtx
#
#
# emp = [[0 for _ in range(2)] for _ in range(2)]
# for _ in range(len(emp)):
#     emp[_][_] = 1
#
# while N:
#     if N & 1:
#         emp = mtx_mul(emp, A, 2, 2)
#     A = mtx_mul(A, A, 2, 2)
#     N //= 2
#
# ans = mtx_mul(emp, u, 2, 1)
#
# print(*ans[1])