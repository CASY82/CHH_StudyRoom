n = int(input())
two = 1
result = 0

for i in range(31):
    if two == n:
        result = 1
        break

    two *= 2

print(result)