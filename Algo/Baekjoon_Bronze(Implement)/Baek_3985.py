import sys

n = int(sys.stdin.readline())
audi = int(sys.stdin.readline())
cake = [0 for _ in range(n)]

max_expect = 0
real_max = 0
result = 0
expect = 0

for i in range(audi):
    start, end = map(int, sys.stdin.readline().split())

    cnt = 0
    if max_expect <= end - start:
        if expect != 0 and max_expect == end - start:
            expect = min(expect, i + 1)
        else:
            expect = i + 1
        max_expect = end - start

    for j in range(start - 1, end):
        if cake[j] == 0:
            cake[j] = i + 1
            cnt += 1

    if real_max < cnt:
        real_max = cnt
        result = i + 1

print(expect)
print(result)