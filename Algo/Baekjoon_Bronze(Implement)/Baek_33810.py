import sys

s = sys.stdin.readline().strip()
check = "SciComLove"
res = 0

for i in range(10):
    if check[i] != s[i]:
        res += 1

print(res)