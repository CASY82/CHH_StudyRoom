hansu = input()
count = 99

if len(hansu) <= 2:
    print(int(hansu))
else:
    for i in range(100, int(hansu)+1):
        check = list(str(i))
        diff = int(check[0]) - int(check[1])

        for j in range(1, len(check)-1):
            if int(check[j]) - int(check[j + 1]) == diff:
                count += 1

    print(count)