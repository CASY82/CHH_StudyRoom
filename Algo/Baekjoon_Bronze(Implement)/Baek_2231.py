n = int(input())
check = False

for i in range(1, n):
    length = len(str(i))
    num = str(i)
    result = 0

    for j in range(length):
        result += int(num[j])

    result += i

    if result == n:
        print(i)
        check = True
        break

if check == False:
    print(0)