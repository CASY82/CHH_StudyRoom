import sys

squad_fir = sys.stdin.readline().strip()
squad_sec = sys.stdin.readline().strip()
res = ""

for i in range(len(squad_fir)):
    res += str(max(int(squad_fir[i]), int(squad_sec[i])))

print(res)