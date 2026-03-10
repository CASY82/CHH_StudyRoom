# 추석은 언제나 좋아
import sys

n = int(sys.stdin.readline())
parents = 0
me = 0

if n >= 1000000:
    parents = int(n * 0.2)
    me = int(n * 0.8)
elif 500000 <= n < 1000000:
    parents = int(n * 0.15)
    me = int(n * 0.85)
elif 100000 <= n < 500000:
    parents = int(n * 0.1)
    me = int(n * 0.9)
else:
    parents = int(n * 0.05)
    me = int(n * 0.95)

print(parents, me)