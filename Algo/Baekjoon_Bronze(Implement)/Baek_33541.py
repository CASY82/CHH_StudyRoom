import sys

year = int(sys.stdin.readline())

check = False
res = 0

while year + 1 < 10000:
    year += 1
    tmp_str = str(year)

    tmp_front = int(tmp_str[:2])
    tmp_back = int(tmp_str[2:])

    if (tmp_front + tmp_back) ** 2 == year:
        res = year
        check = True
        break

if check:
    print(res)
else:
    print(-1)