import sys

n = int(sys.stdin.readline())

# 0, 4, (6, 9) == 1 그러나 0은 맨앞에 올 수 없음
# 1 = 0개
# 8 2개

if n == 0:
    print(1)
elif n == 1:
    print(0)
elif n % 2 == 0:
    for i in range(n // 2):
        print(8, end="")
elif n % 2 == 1:
    print(4, end="")
    for _ in range((n-1) // 2):
        print(8, end="")