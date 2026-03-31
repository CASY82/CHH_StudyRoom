# Минимальная строка
import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

length = len(a)
tmp = a + b
sort_str = sorted(tmp)
res = ""

for i in range(length):
    res = res + sort_str[i]

print(res)