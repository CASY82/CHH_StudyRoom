num_1 = int(input())
num_2 = int(input())

a = num_1 * (num_2 % 10)
b = num_1 * ((num_2 % 100) // 10)
c = num_1 * (num_2 // 100)

print(a)
print(b)
print(c)
print(num_1 * num_2)