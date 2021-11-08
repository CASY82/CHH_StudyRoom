a, b, n = map(int, input().split())
tmp = a % b
count = 0

while n != count:
    result = (tmp * 10) // b
    tmp = (tmp * 10) % b

    count += 1

print(result)