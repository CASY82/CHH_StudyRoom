num = []
max_count = 0
max_count_num = 0

for _ in range(10):
    num.append(int(input()))

for i in range(10):
    if max_count < num.count(num[i]):
        max_count = num.count(num[i])
        max_count_num = num[i]

print(sum(num) // 10)
print(max_count_num)