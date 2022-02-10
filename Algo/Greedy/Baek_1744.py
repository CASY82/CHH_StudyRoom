import sys

n = int(sys.stdin.readline())
plus = []
minus = []
result = 0

for _ in range(n):
    num = int(sys.stdin.readline())

    if num > 0:
        plus.append(num)
    else:
        minus.append(num)

plus.sort()
minus.sort(reverse=True)

while plus:
    if len(plus) >= 2:
        a = plus.pop()
        b = plus.pop()

        if a == 1 or b == 1:
            result += a + b
        else:
            result += a * b
    else:
        result += plus.pop()

while minus:
    if len(minus) >= 2:
        a = minus.pop()
        b = minus.pop()

        result += a * b
    else:
        result += minus.pop()

print(result)