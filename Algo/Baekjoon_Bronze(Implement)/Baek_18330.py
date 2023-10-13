import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

extra = 0
month = 0

if n > (60 + k):
    extra = (n - (60 + k)) * 3000
    month = (60 + k) * 1500
else:
    month = n * 1500

print(extra + month)