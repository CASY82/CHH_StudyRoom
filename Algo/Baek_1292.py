a, b = map(int, input().split())
num = []

for i in range(1, 50):
    for j in range(i):
        num.append(i)

print(sum(num[a-1:b]))