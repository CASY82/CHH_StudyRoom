import sys

# 페르세폴리스
p1, s1 = map(int, sys.stdin.readline().split())
# 에스테그랄
s2, p2 = map(int, sys.stdin.readline().split())

if p1 + p2 == s1 + s2:
    if p2 > s1:
        print("Persepolis")
    elif p2 < s1:
        print("Esteghlal")
    else:
        print("Penalty")
else:
    if p1 + p2 > s1 + s2:
        print("Persepolis")
    else:
        print("Esteghlal")