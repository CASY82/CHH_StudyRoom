import sys

a, b, c = map(int, sys.stdin.readline().split())

#홀수 우선, 큰 수 우선
odd = []
even = []
result = 1

for num in (a, b, c):
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if odd:
    for n in odd:
        result *= n
else:
    for n in even:
        result *= n

print(result)