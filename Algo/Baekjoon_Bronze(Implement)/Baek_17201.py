import sys

n = int(sys.stdin.readline())
magnet = sys.stdin.readline().strip()
check = False

for i in range((n * 2) - 1):
    if magnet[i] == magnet[i - 1]:
        check = True
        break

if check:
    print("No")
else:
    print("Yes")

# 다른 사람 풀이
# n,s=open(0)
# print("YNeos"['11'in s or'22'in s::2])