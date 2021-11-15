n = int(input())
num = []

for i in range(1, int(n ** 0.5)+1):
    if n % i == 0:
        num.append(i)
        num.append(n//i)

print(len(set(num)))