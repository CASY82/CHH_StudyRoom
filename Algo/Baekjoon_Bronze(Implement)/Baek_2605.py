student = int(input())
changer = list(map(int, input().split()))
line = []

for i in range(student):
    line.insert(i - changer[i],i+1)

for j in line:
    print(j, end=' ')