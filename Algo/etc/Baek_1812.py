import sys

n = int(sys.stdin.readline())

candy_sum = 0
tmp = []

for _ in range(n):
    tmp.append(int(sys.stdin.readline()))

candy_sum = sum(tmp) // 2
a1 = candy_sum

for i in range(1, n, 2):
    a1 -= tmp[i]

result = [a1]
tmp_a = a1

for j in range(n-1):
    tmp_a = abs(tmp[j] - tmp_a)
    result.append(tmp_a)

for num in result:
    print(num)