import sys
import re

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
result = 0

tmp = re.findall(r'\d+',word)

for num in tmp:
    result += int(num)

print(result)
