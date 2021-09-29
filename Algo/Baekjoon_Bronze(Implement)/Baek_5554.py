time = []

for i in range(4):
    time.append(int(input()))

result = sum(time)

print(result // 60)
print(result % 60)
