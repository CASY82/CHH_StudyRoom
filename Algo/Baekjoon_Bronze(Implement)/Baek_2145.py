while True:
    num = int(input())
    sum = 0


    if num == 0:
        break

    while True:
        sum += num % 10
        num = num // 10

        if num == 0:
            if sum >= 10:
                num = sum
                sum = 0
            else:
                break

    print(sum)

