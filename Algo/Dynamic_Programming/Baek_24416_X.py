# import sys
# sys.setrecursionlimit(3000000)
#
# n = int(sys.stdin.readline())
# arr = [0, 1, 1] + [0 for i in range(1000000)]
#
# def fibo(n):
#     if n <= 1:
#         return 1
#     elif arr[n] != 0:
#         return arr[n]
#     else:
#         arr[n] = (fibo(n-1) + fibo(n-2)) % 1000000007
#         return arr[n]
#
# print(fibo(n))

#뭐야 엄청쉬운거였다; 어렵게 생각한게 패인...
n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = (a+b)%1000000007, a%1000000007
print(a)

#DP는 이거지...
# import sys
# input = sys.stdin.readline
# dic = dict()
# dic[0] = 0
# dic[1] = 1
# dic[2] = 1
# MOD = 1000000007
# def Fibo(k, dic):
#     if k in dic:
#         return dic[k]
#     n = k // 2
#     fn = Fibo(n, dic)
#     fm = Fibo(n+1, dic)
#     if k % 2 == 0:
#         memo = (fn * (2*fm-fn)) % MOD
#         dic[k] = memo
#     else:
#         memo = (fn**2 + fm**2) % MOD
#         dic[k] = memo
#     return memo
#
# print(Fibo(int(input()), dic))