# Cyanide Rivers
import math
import sys

rivers = sys.stdin.readline().strip()
long_river = 0
tmp = 0

for i in range(len(rivers)):
    if rivers[i] == "0":
        tmp += 1
    else:
        long_river = max(long_river, tmp)
        tmp = 0

print(math.ceil(long_river/2))