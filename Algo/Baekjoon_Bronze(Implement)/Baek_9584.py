import sys
import re

origin_pattern = sys.stdin.readline().strip()
origin_pattern = origin_pattern.replace("*", ".")
result = []

n = int(sys.stdin.readline())
for _ in range(n):
    tmp = sys.stdin.readline().strip()
    if re.search(origin_pattern, tmp):
        result.append(tmp)

print(len(result))
for res in result:
    print(res)