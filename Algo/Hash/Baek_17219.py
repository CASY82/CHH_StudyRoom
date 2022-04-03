import sys

n, m = map(int, sys.stdin.readline().split())
find_account = dict()

for _ in range(n):
    site, password = sys.stdin.readline().strip().split()
    find_account[site] = password

for _ in range(m):
    want_password = sys.stdin.readline().strip()
    print(find_account[want_password])