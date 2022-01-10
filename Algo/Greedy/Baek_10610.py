import sys

n = list(map(int, sys.stdin.readline().strip()))

# 1. 0이 하나 이상 있을 것
# 2. 나머지 숫자를 더했을 때 3의 배수가 나올 것
if 0 in n and sum(n) % 3 == 0:
    n.sort(reverse=True)
    for i in n:
        print(i, end='')
else:
    print(-1)