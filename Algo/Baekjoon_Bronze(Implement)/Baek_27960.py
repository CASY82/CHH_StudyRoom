import sys

a, b = map(int, sys.stdin.readline().split())

a_bin = bin(a)[2:]
b_bin = bin(b)[2:]

a_res = a_bin.zfill(10)
b_res = b_bin.zfill(10)

c_res = ""

for i in range(10):
    if a_res[i] != b_res[i]:
        c_res += "1"
    else:
        c_res += "0"

c_res = c_res[::-1]
result = 0

for i in range(10):
    if c_res[i] == "1":
        result += 2 ** i

print(result)