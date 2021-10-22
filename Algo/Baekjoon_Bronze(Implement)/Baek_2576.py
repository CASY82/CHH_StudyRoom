num = []
odd_num_sum = 0
odd_num = 101


for i in range(7):
    num.append(int(input()))

for j in num:
    if j % 2 == 1:
        odd_num_sum += j

        if odd_num > j:
            odd_num = j

if odd_num > 100:
    print(-1)
else:
    print(odd_num_sum)
    print(odd_num)