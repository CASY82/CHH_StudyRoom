import sys

n = int(sys.stdin.readline())
choose = list(map(int, sys.stdin.readline().split()))
tmp = 0
result = 0

numbers = dict()

for i in range(n):
    numbers[i + 1] = 0

for now in range(n * 2):
    numbers[choose[now]] += 1

    if numbers[choose[now]] == 1:
        tmp += 1
    elif numbers[choose[now]] == 2:
        tmp -= 1

    result = max(result, tmp)

print(result)