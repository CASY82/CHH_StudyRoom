a_card = list(map(int, input().split()))
b_card = list(map(int, input().split()))
result = []

for i, j in zip(a_card, b_card):
    if i == j:
        result.append('D')
    elif i > j:
        result.append('A')
    else:
        result.append('B')

a_count = 0
b_count = 0

for k in result:
    if k == 'A':
        a_count += 3
    elif k == 'B':
        b_count += 3
    else:
        a_count += 1
        b_count += 1

print(a_count, b_count, end=' ')
print()

if a_count > b_count:
    print('A')
elif b_count > a_count:
    print('B')
else:
    check = False
    for z in range(len(result) - 1, 0, -1):
        if result[z] == 'A':
            print('A')
            check = False
            break
        elif result[z] == 'B':
            print('B')
            check = False
            break
        else:
            check = True

    if check:
        print('D')