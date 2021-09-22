n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

if num[1] - num[0] == num[2] - num[1]:
    diff = num[1] - num[0]
    result = num[len(num) - 1] + diff
else:
    r = num[1] // num[0]
    result = num[len(num) - 1] * r

print(result)