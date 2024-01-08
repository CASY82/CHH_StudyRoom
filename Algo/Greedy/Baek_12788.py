import sys

n = int(sys.stdin.readline())
m, k = map(int, sys.stdin.readline().split())

pen = list(map(int, sys.stdin.readline().split()))

total_people = m * k
pen.sort(reverse=True)

tmp = 0
result = 0
check = False

for borrow in pen:
    tmp += borrow
    result += 1

    if total_people <= tmp:
        check = True
        break

if check:
    print(result)
else:
    print("STRESS")