num = input()
result = 0

for i in range(len(num)):
    result += (int(num[i]) ** 5)

print(result)