l = int(input())
s = list(map(int, input().split()))
n = int(input())
A = 0
B = 0
count = 0

s.sort()
for i in range(len(s)):
    if s[i] < n:
        A = s[i]
        B = s[i + 1]
    elif s[i] == n:
        break
    else:
        if s[0] > n:
            A = 0
            B = s[0]


for i in range(A + 1, n + 1):
    for j in range(n, B):
        if i == j:
            continue

        count += 1


print(count)

#수학적으로 푼 사람 풀이
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# L = sorted(list(map(int, input().split())))
# k = int(input())
# if k in L: print(0)
# else:
#     L += [k]
#     L.sort()
#     a = L.index(k)
#     if a == 0:
#         print(k * (L[1] - k) - 1)
#     else:
#         x, y = L[a-1], L[a+1]
#         print((k-x)*(y-k)-1)