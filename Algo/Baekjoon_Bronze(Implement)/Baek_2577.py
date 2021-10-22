a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)
num_count = [0 for i in range(10)]

for i in range(10):
    num_count[i] = result.count(str(i))

for i in range(10):
    print(num_count[i])