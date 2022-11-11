import sys

num = dict()
n = int(sys.stdin.readline())

for _ in range(n):
    put_num = int(sys.stdin.readline())

    if put_num not in num:
        num[put_num] = 1
    else:
        num[put_num] += 1

tmp = [k for k,v in num.items() if max(num.values()) == v]
print(min(tmp))