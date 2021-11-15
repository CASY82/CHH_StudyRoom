#1트에 통과~
n, m = map(int, input().split())
array1 = []
array2 = []
count = 0
check = False

for i in range(n):
    array1.append(list(input()))

for i in range(n):
    array2.append(list(input()))

#연산하는 부분
for a in range(n-2):
    for b in range(m-2):
        if int(array1[a][b]) ^ int(array2[a][b]) == 1:
            for i in range(a, a+3):
                for j in range(b, b+3):
                    if array1[i][j] == '1':
                        array1[i][j] = '0'
                    else:
                        array1[i][j] = '1'

            count += 1

        if array1 == array2:
            break

if array1 == array2:
    check = True
else:
    check = False

if check:
    print(count)
else:
    print(-1)

