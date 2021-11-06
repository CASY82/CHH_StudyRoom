fbi = []
result = []

for _ in range(5):
    fbi.append(input())

for i in fbi:
    if 'FBI' in i:
        result.append(fbi.index(i))

if result:
    for j in result:
        print(j+1, end=' ')
else:
    print('HE GOT AWAY!')