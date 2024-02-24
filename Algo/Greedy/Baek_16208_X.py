import sys

# 아이디어는 (전체 - 최소 배열 요소) 이걸 계속 진행해 나가는 방식이다.
n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
result = 0

number.sort()
total = sum(number)

for i in range(n):
    result += number[i] * (total - number[i])
    total -= number[i]

print(result)