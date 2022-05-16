import sys

num = list(sys.stdin.readline().strip())

cnt = 0

while len(num) > 1:
    tmp = 1

    for num_t in num:
        tmp *= int(num_t)

    num = list(str(tmp))
    cnt += 1

print(cnt)