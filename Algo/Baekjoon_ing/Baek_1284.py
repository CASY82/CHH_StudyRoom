while True:
    num = input()
    result = 0

    if num == '0':
        break

    #1 -> 2 0 -> 4 나머지 3
    for i in num:
        if i == '1':
            result += 2
        elif i == '0':
            result += 4
        else:
            result += 3

    print(result + 2 + len(num) - 1)