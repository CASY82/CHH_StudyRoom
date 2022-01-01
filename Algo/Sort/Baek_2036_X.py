#양수 음수를 분리하여 처리하는 부분을 생각 못해서 못풀고 있었음.. 전체적인 로직 참고를 좀 하였으므로
#해당 문제는 못푼문제...
import sys

n = int(sys.stdin.readline())
numList_plus = []
numList_minus = []
numList_zero = []
result = 0

# 양음 분리할것
for _ in range(n):
    number = int(sys.stdin.readline())

    if number > 0:
        numList_plus.append(number)
    elif number < 0:
        numList_minus.append(number)
    else:
        numList_zero.append(number)

numList_plus.sort()
numList_minus.sort(reverse=True)

# 1. 양 * 양 / 음 * 음 / 양 + 음
# 3. 1 + 양 / 1 + 음(얘는 어차피 맨 마지막에 처리해도 됨)
while len(numList_plus) > 1:
    a = numList_plus.pop()
    b = numList_plus.pop()

    if b == 1:
        result += a + b
    else:
        result += a * b

while len(numList_minus) > 1:
    a = numList_minus.pop()
    b = numList_minus.pop()

    result += a * b

# 2. 0 + 양 / 0 * 음
if numList_zero:
    if numList_minus:
        a = numList_zero.pop()
        b = numList_minus.pop()
        result += a * b

if numList_zero:
    if numList_plus:
        a = numList_zero.pop()
        b = numList_plus.pop()
        result += a + b

# 나머지 남은 녀석들은 그냥 더한다.
if numList_plus:
    a = numList_plus.pop()

    result += a

if numList_minus:
    a = numList_minus.pop()
    result += a

print(result)
# 5
# -4
# 3
# 1
# 0
# -8
#
# [-8, -4, 0, 1, 3]
# answer 36
#
# 2
# 0
# -1
#
# [0, -1]
# answer 0
#
# 5
# 5
# 4
# 3
# 0
# -3
#
# [-3, 0, 3, 4, 5]
# answer 23