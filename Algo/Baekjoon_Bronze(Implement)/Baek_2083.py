member = []
division = ['Junior', 'Senior']

while True:
    tmp = []
    name, age, weight = input().split()

    if name == '#':
        break

    tmp.append(name)
    tmp.append(int(age))
    tmp.append(int(weight))
    member.append(tmp)

for i in range(len(member)):
    if member[i][1] > 17 or member[i][2] >= 80:
        print(member[i][0], division[1])
    else:
        print(member[i][0], division[0])