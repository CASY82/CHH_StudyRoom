import sys

su = list(map(int, sys.stdin.readline().split()))
us = list(map(int, sys.stdin.readline().split()))

us.sort()
su.sort()

res = 0

for i in range(len(su)):
    if su[i] > us[i]:
        res += 1

print(res)