while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if (b - a) == (c - b) and b-a != 0:
        result_word = 'AP'
        next_num = c + (c - b)
    else:
        result_word = 'GP'
        next_num = c * (c // b)

    print(result_word, next_num)