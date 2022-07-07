import sys

n, m = map(int, sys.stdin.readline().split())

# 뉴비 : 1, 2학년
# 올드비 : 1, 2가 아니면서 n 학년 이하
# TLE : n 학년 이상

if m == 1 or m == 2:
    print("NEWBIE!")
elif 2 < m <= n:
    print("OLDBIE!")
else:
    print("TLE!")