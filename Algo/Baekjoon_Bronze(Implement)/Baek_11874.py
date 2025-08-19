import sys

l = int(sys.stdin.readline())
d = int(sys.stdin.readline())
x = int(sys.stdin.readline())

data = []

for i in range(l, d + 1):
    tmp = i
    tmp_res = 0

    while tmp > 0:
        tmp_res += tmp % 10
        tmp //= 10

    if tmp_res == x:
        data.append(i)

print(min(data))
print(max(data))