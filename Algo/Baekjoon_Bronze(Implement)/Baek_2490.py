for _ in range(3):
    yut = list(map(int, input().split()))

    result = yut.count(0)

    if result == 4:
        print('D')
    elif result == 3:
        print('C')
    elif result == 2:
        print('B')
    elif result == 1:
        print('A')
    else:
        print('E')