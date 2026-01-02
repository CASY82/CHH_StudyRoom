import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

if a + c < b + d:
    print("Hanyang Univ.")
elif a + c > b + d:
    print("Yongdap")
else:
    print("Either")