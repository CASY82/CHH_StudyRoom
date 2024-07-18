import sys

m = int(sys.stdin.readline())

for _ in range(m):
    set_menu = list(sys.stdin.readline().strip().split())

for menu in set_menu:
    print(menu)

# 다른 사람 풀이
# a,b,*_=open(0)
# print(b)