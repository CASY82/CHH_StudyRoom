n = int(input())
num_str = ''

for i in range(1, n + 1):
    num_str += str(i)

print(num_str.find(str(n)) + 1)