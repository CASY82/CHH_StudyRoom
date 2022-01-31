import sys

i = 0

while True:
    l, p, v = map(int, sys.stdin.readline().split())
    i += 1

    if l + p + v == 0:
        break

    full =  (v // p) * l
    remainer = min(v % p, l)
    result = full + remainer

    print("Case ", i, ": ", result, end="", sep="")
    print()