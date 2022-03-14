import re
import sys

# 정규 표현식을 배우자!
m = int(sys.stdin.readline())
numbers = []

for _ in range(m):
    word = sys.stdin.readline().strip()

    numbersTmp = re.findall(r'\d+', word)

    for num in numbersTmp:
        numbers.append(int(num))

numbers.sort()
for i in numbers:
    print(i)