import sys

n = int(sys.stdin.readline())

res = ""

tmp_five = n // 5
tmp = n % 5

for _ in range(tmp_five):
    res += "V"

for _ in range(tmp):
    res += "I"

print(res)