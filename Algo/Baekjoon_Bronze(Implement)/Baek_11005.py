import sys

changer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
result = []

num, notation = map(int, sys.stdin.readline().split())

while num > 0:
    result.append(changer[num % notation])

    num //= notation

result.reverse()

for i in range(len(result)):
    print(result[i], end="")