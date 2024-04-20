import sys

fir = sys.stdin.readline().strip()
sec = sys.stdin.readline().strip()

res = list(fir + sec)
res.sort()

print("".join(res))