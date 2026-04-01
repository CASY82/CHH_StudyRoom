# Расписание
import sys

n = int(sys.stdin.readline())
deadline = list(map(int, sys.stdin.readline().split()))

new_array = []

for i in range(n):
    new_array.append((i, deadline[i]))

new_array.sort(key=lambda x:x[1])

res = [0] * n

for j in range(n):
    res[new_array[j][0]] = j + 1

print(*res)