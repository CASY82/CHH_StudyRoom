num = []
max_val = 0
index = 0

for _ in range(9):
    num.append(list(map(int, input().split())))

for i in range(9):
    if max(num[i]) > max_val:
        max_val = max(num[i])
        index = i

print(max_val)
print(index + 1, num[index].index(max_val) + 1)