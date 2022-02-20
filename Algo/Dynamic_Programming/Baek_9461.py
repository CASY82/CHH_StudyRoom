import sys

t = int(sys.stdin.readline())
arr = [0, 1, 1, 1] + [0] * 100

for i in range(3, 101):
    arr[i] = arr[i-2] + arr[i-3]

for _ in range(t):
    print(arr[int(sys.stdin.readline())])

# 메모이제이션 사용
# from sys import stdin
# input = stdin.readline
#
# def memoization(n):
#   if n < 1: return 0
#   if dp[n]: return dp[n]
#   dp[n] = memoization(n - 1) + memoization(n - 5)
#   return dp[n]
#
#
# dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
# for tc in range(int(input())):
#   N = int(input())
#   print(memoization(N))