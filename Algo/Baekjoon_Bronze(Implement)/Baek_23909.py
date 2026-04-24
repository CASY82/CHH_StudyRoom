# Record Breaker

import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
     n = int(sys.stdin.readline())
     v = list(map(int, sys.stdin.readline().split()))

     now_max = -1
     res = 0

     for i in range(n):
         if v[i] > now_max:
            now_max = v[i]

            if i < n - 1 and v[i + 1] < v[i]:
                 res += 1
            elif i == n - 1:
                 res += 1

     print("Case #{0}: {1}".format(case, res))